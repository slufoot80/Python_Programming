import pytest


from pgbackup import cli

url = "postgres://bob:2Jee6Ngi@example.com:5432/db_one"

def test_parser_without_driver():
    """
    Without a specified driver the parser will exit
    """
    with pytetst.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])
