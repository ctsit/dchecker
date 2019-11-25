CHANGELOG
=========

2019-11-25 v2.0.0-rc1
---------------------

Complete rewrite for Python 3.

Note for UF personnel: this will be a public release and all queries have been
separated and moved into a private repository. Only code changes will occur in
this repository.


2019-09-10 v1.6.0
-----------------

Improved queries that grouped by strings.

 * Update queries to cast strings to xsd before grouping. (Hunter Jarrell)


2019-08-27 v1.5.0
-----------------

Added new queries

 * Add queries that count duplicate ISSNs and EISSNs. (Taeber Rapczak)
 * Add security query for privacy flag. (Hunter Jarrell)
 * Add query to find UFEntities without gatorlinks. (Naomi Braun)
 * Add query that counts organizations with same name. (Taeber Rapczak)


2019-04-09 v1.4.0
-----------------

Added more queries and ability to change Report subject.

 * Add warning about bad logic in run_query (Taeber Rapczak)
 * Cleanup run_query function as per PEP-8 (Taeber Rapczak)
 * Handle case of COUNT queries returning 0 (Taeber Rapczak)
 * Add query for people with multiple primary emails. (Hunter Jarrell)
 * Rename old datetime query to be more accurate and add actual orphan datetime query (Naomi Braun)
 * Add ability to change the report's subject (Taeber Rapczak)
 * Add query to count wrongly-typed authorships (Taeber Rapczak)


2019-03-15 v1.3.1
-----------------

Hotfix for bug causing early termination of code.


2019-03-14 v1.3.0
-----------------

Added configuration option for query folder and new queries

 * Move security related queries; add configurable queries location. (Taeber Rapczak)
 * Update ranges of protected departments. (Hunter Jarrell)
 * Add query for individuals of blank type. (Taeber Rapczak)


2019-02-25 v1.2.0
-----------------

Added new queries

 * Add query for getting count of orphaned datetimes (Naomi Braun)
 * Add query for checking malformed ISSNs (Naomi Braun)
 * Add query for count of Duplicated Emails. (Hunter Jarrell)
 * Add query for VCards w/o associations. (Hunter Jarrell)
 * Add query for Email Attributes without Emails. (Hunter Jarrell)
 * Add query to find VCard attributes without VCards. (Hunter Jarrell)
 * Add query to find VCards with multiple people. (Hunter Jarrell)
 * Add query for GatorLink on non-person (Taeber Rapczak)
 * Add query to find empty emails (Hunter Jarrell)
 * Add query for finding emails with html tags. (Hunter Jarrell)
 * Add query to find UF people missing UFEntity (Taeber Rapczak)
 * People with more than one gatorlink. (Hunter Jarrell)
 * Add count of articles with duplicate PMIDs. (Hunter Jarrell)


2019-01-15 v1.1.0
-----------------

Added new queries

 * New query: Articles with too many labels (Taeber Rapczak)
 * New query: Authorship with wrong relation count (Taeber Rapczak)
 * New query: Authorship without authors (Taeber Rapczak)
 * New query: Gatorlinks with HTML tags (Hunter Jarrell)
 * New query: Person without name (Taeber Rapczak)


2018-12-11 v1.0.0
-----------------

Added new queries

 * New query: Check DOIs for HTML tags (Hunter Jarrell)
 * New query: Check PMIDs for non-number characters (Hunter Jarrell)
 * New query: Get journals without labels (Hunter Jarrell)
 * Edit query: Edit Journals_with_multiple_labels variable name so that Journal URI is put into email (Hunter Jarrell)
 * New query: Find people with very very too long names (Taeber Rapczak)
 * New query: Find people who have been merged with articles (Hunter Jarrell)


2018-05-21 v0.5.3
-----------------

Updated license and authors file.

 * Added CONFIG argument. (Nicholas Rejack)
 * Now dchecker reports version number with a command line argument. Changing dchecker/version.py updates version number globally. (Nicholas Rejack)
 * Changed directory structure to use dchecker/ directory. Added __init__ with version number. (Nicholas Rejack)
 * File cleanup. Removing unused error queries directory. (Nicholas Rejack)


2015-11-17 v0.5.2
-----------------

Added new query for journals with multiple labels.

  * Adding new query to find Journals with multiple labels. (Nicholas Rejack)


2015-11-03 v0.5.1
-----------------

Fixes for error reporting and packaging.

 * Added fix for error report. run_query_new function wasn't returning the errors when encountered. (Nicholas Rejack)
 * Fixing packaging. Now doesn't cause error on exit. (Nicholas Rejack)


2015-11-03 v0.5.0
-----------------

First tagged release. Many improvements, especially in install procedure.

 * Updating README to reflect new install instructions. (Nicholas Rejack)
 * Updating setup.py for new method. Uses an egg file. (Nicholas Rejack)
 * Adding LICENSE.txt license file. Using BSD 3-Clause. (Nicholas Rejack)
 * Removing test.txt (previous record of pylint run) (Nicholas Rejack)
 * Adding pylintrc that stores pylint configuration. Prevents pylint alerting on variable names that are not constants. (Nicholas Rejack)
 * Modifies dchecker.py to improve pylint score, including new docstrings. New score 10/10. (Nicholas Rejack)
 * Fixed numerous pylint errors. New score 6.37/10. (Nicholas Rejack)
 * Fixed indentation and other errors in dchecker.py to bring up pylint score. New score 5.11/10. (Nicholas Rejack)
 * updated formatting for run_new_query function (atloiaco)
 * Roll back faulty merge on dchecker.py (Nicholas Rejack)
 * Corrects variable name deptID to DeptID in queries/Duplicated_deptIDs.rq (Nicholas Rejack)
 * Changed capitalization on query files to be consistent. (Nicholas Rejack)
 * Updated queries to make capitalization consistent and ASCII sortable. (Nicholas Rejack)
 * Fixes indentation in dchecker.py. (Nicholas Rejack)
 * Adding AUTHORS.md file with name of authors. (Nicholas Rejack)
 * added new logging to dchecker to show which query is currently running (Nicholas Rejack)
 * updated query for no last name. (Nicholas Rejack)
 * updated readme file (Alex Loiacono)
 * Refactoring directory structure and removing backups of .py files. (Nicholas Rejack)
 * new version of vivotools.py. (Nicholas Rejack)
 * added new logging to dchecker to show which query is currently running (Nicholas Rejack)
 * commented out Bio module in vivotools.py. not required for this app. (Nicholas Rejack)
 * switched sort order in Authorship query to improve performance. (Nicholas Rejack)
 * changed non-UF organization query to all organizations. Non-UF version non-performant. (Nicholas Rejack)
 * fixing missing elements in 2 queries. Needed prefixes. (Nicholas Rejack)
 * updated unlinked authorships query with foaf prefix. (Nicholas Rejack)
 * removed unneeded queries. new ontology doesn't require dual linking for these. (Nicholas Rejack)
 * updated UFPD position query. (Nicholas Rejack)
 * updated position in ACS query (Nicholas Rejack)
 * updated missing person in position query (Nicholas Rejack)
 * Updated missing organization for position query. (Nicholas Rejack)
 * moved Authorships and Information Resources query (Nicholas Rejack)
 * updated readme file (Alex Loiacono)
 * updated query to find authorships not linked to authors. (Nicholas Rejack)
 * updated query for no last name. (Nicholas Rejack)
 * updated ACS organization for position query. (Nicholas Rejack)
 * updated ACS organization for position query. (Nicholas Rejack)
 * updated query for UF people with display name but no last name to use vcard structure. (Nicholas Rejack)
 * removed unused public key file (Nicholas Rejack)
 * add non uf organization (Anurag Soni)
 * clean up the source directory by removing old queries (Anurag Soni)
 * fix non_uf_organizations and count_name_prefixes query (Anurag Soni)
 * fix query for URIs (Anurag Soni)
 * revert to old function for queries with less than 3 columns (Anurag Soni)
 * add new sparql query to count name prefixes (Anurag Soni)
 * Made column heading more readable by using case (Alex Loiacono)
 * fixed formatting for duplicate UFID and gatorlink (Anurag Soni)
 * Set config back to group address. (Erik C. Schmidt)
 * Changed variable name to mixed case. (Erik C. Schmidt)
 * updated formatting for duplicate UFID and gatorlink (Anurag Soni)
 * duplicated gatorlink and ufid query fixed (Anurag Soni)
 * Changed debug.cfg to group email address for testing (Erik C. Schmidt)
 * backup of the old queries (nitinkosuri)
 * backup of the old queries (nitinkosuri)
 * modified queries - removed count of number of records (nitinkosuri)
 * Revert "backup of the old queries" (nitinkosuri)
 * backup of the old queries (nitinkosuri)
 * Modified config files to send from please-do-not-reply@ufl.edu (Erik C. Schmidt)
 * .gitignore is now working (Nicholas Rejack)
 * update (Nicholas Rejack)
 * changed name of readme (Nicholas Rejack)
 * first trial at using distutils (Nicholas Rejack)
 * removed wrongly titled query (Nicholas Rejack)
 * updated error query (Nicholas Rejack)
 * re-adding queries (Nicholas Rejack)
 * adding code to read query into report (Nicholas Rejack)
 * updated logging messages (Nicholas Rejack)
 * updated to use new directory struture (Nicholas Rejack)
 * UF_people_with_display_name_but_no_last_name.rq (Nicholas Rejack)
 * updated dchecker to reflect config dir (Nicholas Rejack)
 * moved config files to config dir and added UFVIVOTECH to prod (Nicholas Rejack)
 * added name parts query (Nicholas Rejack)
 * changed variable output name in UF multiple label query (Nicholas Rejack)
 * catchup commit (Nicholas Rejack)
 * add new, currently unworking query (Nicholas Rejack)
 * remove CHANGELOG.txt (Nicholas Rejack)
 * added *.log to .gitignore (Nicholas Rejack)
 * updated query files and log name (Nicholas Rejack)
 * Added text to the CHANGELOG (Mike Conlon)
 * Creating a new CHANGELOG file (Mike Conlon)
 * Added a comment to the description of vivo (Mike Conlon)
 * added basic logging functionality (Nicholas Rejack)
 * updated readme (Nicholas Rejack)
 * updated readme with config info (Nicholas Rejack)
 * updated config file (Nicholas Rejack)
 * updated readme (Nicholas Rejack)
 * catch case where user provides no config file (Nicholas Rejack)
 * correcting smtplib typo (Nicholas Rejack)
 * updated to add configuration files (Nicholas Rejack)
 * updated .gitignore to ignore python byte code files (Nicholas Rejack)
 * updated readme (Nicholas Rejack)
 * updated readme to use markdown (Nicholas Rejack)
 * readding public key (Nicholas Rejack)
 * added debug mode and ACS queries (Nicholas Rejack)
 * added 4 ACS queries (Nicholas Rejack)
 * modified UFPD queries to find via deptID (Nicholas Rejack)
 * changed name of source file to dchecker.py (Nicholas Rejack)
 * added keys (Nicholas Rejack)
 * changes from MC email (Nicholas Rejack)
 * replaced report email address to UFVIVOTECH-L (Nicholas Rejack)
 * changed report format so that numbers line up on (Nicholas Rejack)
 * moved to dchecker.py, added new methods, and external query files (Nicholas Rejack)
 * adding vivotools.py (Nicholas Rejack)
 * adding vivotools.py (Nicholas Rejack)
 * adding vivotools lib (Nicholas Rejack)
 * added new queries and improved reporting function (Nicholas Rejack)
 * added main program file (Nicholas Rejack)
 * Initializing dcheckerapp repository (nrejack)
