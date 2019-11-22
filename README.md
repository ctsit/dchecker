DChecker
========

*DChecker* is a tool for running data integrity queries for
[VIVO](http://www.vivoweb.org).

It scans a directory for SPARQL query files, runs each one sequentially, then
emails a report.

Version 2 was a complete rewrite for Python 3.


Quickstart
----------

    $ pip3 install git+https://github.com/ctsit/dchecker.git
    $ dchecker https://sparql.school.edu/ ./queries


Configuration
-------------

All configuration is done using command-line arguments. For more information,
look at the usage in `dchecker.py` or run:

    $ dchecker --help


Adding new queries
------------------

Queries are run sequentially out of the `queries` folder. To add a new SPARQL
query, save it with the `.rq` file extension, and it will be run automatically
when DChecker runs.


Contributing
------------

We welcome contributions! Please be aware, however, that we can only accept your
code contributions (or other sources) if you affirm that the work is your own
and that you are assigning copyright to the *University of Florida*.
