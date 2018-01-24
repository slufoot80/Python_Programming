pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

Preparing for Development
-------------------------

Ensure 'pip' and 'pipenv' are installed
Clone the repository 'git clone git@github:example/pgbackup'
Fetch Development dependencies: make install

Usage
-----

Pas in a full database url the sotrage driver, and destination.

S3 Example with bucket name:
   $ pgbackup postgres://bob@example:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run Test locally using 'make' if virtualenv is active:
  $ make

if virtualenv isn't active then use:

    $ pipenv run make 
