CHANGELOG
=========

## v2.1.2 - 2023-05-03
## Added
 * Added `ENDPOINT_ALIAS` to override `Endpoint` in the generated report 

## Fixed
 * Pass proper header to receive json response

## v2.1.1 - 2023-05-03
## Added
 * Load environment variables on run (Michael Bentz)

## v2.1.0 - 2023-05-01
## Added
 * Add launch.json (Michael Bentz)
 * Add dev improvements (Michael Bentz)
 * Add gitignore (Michael Bentz)

## Changed
 * Use toml instead of setup.py (Michael Bentz)

## Fixed
 * Close Update sample endpoint in README #1. (Michael Bentz)

2019-11-27 v2.0.1
-----------------

Bug fix.

* Support queries that return only one untyped value (Taeber Rapczak)


2019-11-26 v2.0.0
-----------------

Complete rewrite for Python 3.

Note for UF personnel: this will be a public release and all queries have been
separated and moved into a private repository. Only code changes will occur in
this repository. See dchecker-v1's CHANGELOG for previous changes.

