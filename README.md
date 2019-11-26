DChecker
========

*DChecker* is a tool for running data integrity queries for
[VIVO](http://www.vivoweb.org).

It scans a directory for SPARQL query files, runs each one sequentially, then
emails a report.


Quickstart
----------

    $ pip3 install git+https://github.com/ctsit/dchecker.git
    $ dchecker https://sparql.school.edu/ ./queries

*Note:* a report is printed to STDOUT and log messages are printed to STDERR.


Configuration
-------------

All configuration is done using command-line arguments. For more information,
look at the usage in `dchecker.py` or run:

    $ dchecker --help


Adding new queries
------------------

Queries are run sequentially from a specified folder (or the current folder
if unspecified).

To add a new SPARQL query, save it in the same folder as your other queries with
the `.rq` extension, and it will be included automatically when DChecker runs.


Contributing
------------

We welcome contributions.

Please be aware that by submitting pull requests, or contributing your code in
some other way, you affirm that the work is your own and that you are assigning
copyright to the University of Florida.

Furthermore, explain how you tested your changes and be sure to match the
existing style.
