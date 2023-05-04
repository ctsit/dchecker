""" Data integrity checker for VIVO

Copyright 2019 University of Florida.

USAGE: dchecker -h|--help
       dchecker --version
       dchecker <endpoint> [<queries>]
       dchecker <endpoint> <smtp> <from> <to>[,<to>...]
       dchecker <endpoint> <smtp> <from> <to>[,<to>...] <queries> [<subject>]

DChecker is an open-source (MIT License) tool for running data integrity
queries for VIVO.

DChecker scans a directory for SPARQL query files, runs each one sequentially,
then emails a report.

The first form will simply print this usage.

The second form will simply print the version number.

The next form will run each query and print the report to STDOUT and verbose
messages to STDERR.

  endpoint   URL to the SPARQL endpoint to query against
  queries    Path to the folder containing the SPARQL queries.
             Defaults to ".".

The finally forms will run the queries and email a report.

  smtp       Outgoing mail server
  from       Email address of the sender
  to         Email addresses of recipients separated by commas.
  subject    Subject for the report. Use "%c" for current date and time.
             Defaults to "VIVO Data Quality report for %c".

Please be aware there are some default prefixes to simplify SPARQL queries.
"""

from email.mime.text import MIMEText
from dotenv import load_dotenv
import datetime
import json
import glob
import os
import os.path
import smtplib
import sys
import traceback
import typing
import urllib.parse
import urllib.request


DEFAULT_PREFIXES = """
    PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>
    PREFIX owl:     <http://www.w3.org/2002/07/owl#>
    PREFIX swrl:    <http://www.w3.org/2003/11/swrl#>
    PREFIX swrlb:   <http://www.w3.org/2003/11/swrlb#>
    PREFIX vitro:   <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#>
    PREFIX bibo:    <http://purl.org/ontology/bibo/>
    PREFIX dcelem:  <http://purl.org/dc/elements/1.1/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX event:   <http://purl.org/NET/c4dm/event.owl#>
    PREFIX foaf:    <http://xmlns.com/foaf/0.1/>
    PREFIX geo:     <http://aims.fao.org/aos/geopolitical.owl#>
    PREFIX pvs:     <http://vivoweb.org/ontology/provenance-support#>
    PREFIX ero:     <http://purl.obolibrary.org/obo/>
    PREFIX scires:  <http://vivoweb.org/ontology/scientific-research#>
    PREFIX skos:    <http://www.w3.org/2004/02/skos/core#>
    PREFIX ufVivo:  <http://vivo.ufl.edu/ontology/vivo-ufl/>
    PREFIX vitro:   <http://vitro.mannlib.cornell.edu/ns/vitro/public#>
    PREFIX vivo:    <http://vivoweb.org/ontology/core#>
    PREFIX core:    <http://vivoweb.org/ontology/core#>
"""

VERSION = "2.2.0"

XSD_INTEGER = "http://www.w3.org/2001/XMLSchema#integer"


def is_safe_request(endpoint: str, email: str | None, password: str | None):
    if "http:" in endpoint and "localhost" not in endpoint:
        if (email != "" and email is not None) or (password != "" and password is not None):
            return False
    return True


def log(file: str, msg: str):
    """Prints out a log message in a consistent format."""
    print(f"{file}: {datetime.datetime.now().isoformat()}: {msg}",
          file=sys.stderr)


def main():
    """Program entry."""
    argc = len(sys.argv)

    if argc <= 1:
        usage(2)

    if sys.argv[1] in ["-h", "--help"]:
        usage(0)

    if sys.argv[1] == "--version":
        print(VERSION)
        sys.exit(0)

    # Set some defaults then override them using any command-line arguments.
    endpoint = sys.argv[1]
    queries = "."
    smtp = ""
    sender = ""
    recipients = ""
    subject = "VIVO Data Quality report for %c"

    if argc == 3:
        queries = sys.argv[2]
    elif argc >= 6:
        smtp, sender, recipients, queries = sys.argv[2:6]

    if argc >= 7:
        subject = ' '.join(sys.argv[6:])

    load_dotenv()
    if not is_safe_request(endpoint, os.getenv("EMAIL"), os.getenv("PASSWORD")):
        print(
            "Passing credentials is not supported for http."
            "Either remove EMAIL and PASSWORD from .env or use https."
        )
        exit()

    started = datetime.datetime.now().replace(microsecond=0)

    try:
        results = run(endpoint, queries)
    except Exception:
        traceback.print_exc()
        results = "Error! Check the system logs."

    done = datetime.datetime.now().replace(microsecond=0)

    subject = subject.replace("%c", started.isoformat(sep=" "), 1)

    target_endpoint = endpoint

    endpoint_alias = os.getenv("ENDPOINT_ALIAS")
    if endpoint_alias is not None or endpoint_alias:
        target_endpoint = endpoint_alias

    report = f"""
{subject}
  Endpoint: {target_endpoint}
  Started : {started.isoformat(sep=" ")}
  Finished: {done.isoformat(sep=" ")}
  Runner  : dchecker v{VERSION}

{results}
"""
    print(report)

    if smtp and sender and recipients:
        print(f"Emailing report to {recipients} from {sender} using {smtp}.",
              file=sys.stderr)
        send_report(smtp, report, subject, sender, recipients)

    print("Done.", file=sys.stderr)


def pretty_name(filename: str) -> str:
    """Returns a version of `filename` that is easier for a human to read."""
    return os.path.basename(filename).replace("_", " ").replace(".rq", "")


def query(endpoint: str, query: str, prefixes: str = DEFAULT_PREFIXES) -> dict:
    """Queries a SPARQL endpoint and returns the JSON-formatted results."""

    params = {
        "query": prefixes+query,
        "format": "json",
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }
    encoded = urllib.parse.urlencode(params).encode("UTF-8")

    headers = {
        'Accept': 'application/sparql-results+json'
    }

    request = urllib.request.Request(endpoint, headers=headers, data=encoded, method="POST")

    with urllib.request.urlopen(request) as response:
        body = response.read()
        resp = json.loads(body)
        return resp


def run(endpoint: str, queries: str) -> str:
    """Runs all queries and returns results in the expected report format."""

    print(f"Querying {endpoint} with files found in: {queries}",
          file=sys.stderr)

    report = ""
    results: typing.Dict[str, dict] = {}
    errors: typing.Dict[str, str] = {}

    files = glob.iglob(os.path.join(queries, "*.rq"))
    files = sorted(files)
    print(f"Files found: {len(files)}", file=sys.stderr)
    for file in files:
        print(f"- {file}", file=sys.stderr)

    for file in files:
        with open(file) as fp:
            log(file, "started")
            try:
                sparql = fp.read()
                response = query(endpoint, sparql)
                values = response["results"]["bindings"]
                results[file] = values
                log(file, str(len(values)))
                log(file, "done")
            except Exception as ex:
                traceback.print_exc()
                log(file, f"ERROR! {ex}")
                errors[file] = str(ex)
                continue

    for file, values in results.items():
        count = len(values)

        # Check to see if an empty result set is returned.
        if count == 0 or (count == 1 and not values[0]):
            report += two_columns("0", pretty_name(file))
            continue

        if len(values[0].keys()) > 1:
            print(f"WARNING! {file} returns multiple columns; expected 1.",
                  file=sys.stderr)

        col = next(iter(values[0].keys()))

        # If the query returned a single number, like from COUNT(), use it.
        if count == 1 and values[0][col].get("datatype", "") == XSD_INTEGER:
            value = values[0][col]["value"]
            report += two_columns(value, pretty_name(file))
            continue

        # Otherwise, print out the count.
        report += two_columns(str(count), pretty_name(file))
        if count < 20:
            for v in values:
                report += two_columns("", "  " + v[col]["value"])

    for file, err in errors.items():
        report += two_columns("Error!", pretty_name(file))
        report += two_columns("", "  " + str(err))

    return report


def send_report(host: str, report: str, subject: str, sender: str,
                recipients: str):
    """Emails the report."""

    msg = MIMEText(report, "plain")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipients

    with smtplib.SMTP(host) as smtp:
        errors = smtp.sendmail(sender, recipients, msg.as_string())
        for recipient, (code, err) in errors.items():
            print(f"Error sending report to {recipient}: {code} - {err}")


def two_columns(first: str, second: str) -> str:
    """Formats first and second in the two-column report format."""
    return f"  {first:7}  {second}\n"


def usage(status: int):
    """Prints the usage text and exits."""
    print(__doc__.strip())
    print(DEFAULT_PREFIXES)
    sys.exit(status)


if __name__ == "__main__":
    main()
