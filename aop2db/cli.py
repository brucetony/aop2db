"""Console script for aop2db."""
import sys
import click
import logging

from sqlalchemy import create_engine

from aop2db.utils import set_conn
from aop2db.aop.importer import import_aop_data

logger = logging.getLogger(__name__)


@click.group(help=f"AOP2DB Database Framework Command Line Utilities on {sys.executable}")
@click.version_option()
def main():
    """Console script for aop2db."""
    pass


@main.command()
def load():
    """Downloads the AO wiki data and imports into the relational database."""
    import_aop_data()


@main.command()
@click.argument('conn_str')
def conn(conn_str: str):
    """Sets the SQL connection string in the configuration file.

    Parameters
    ----------
    conn_str : str
        A python compatible SQL connection string. Drivers (e.g. pymysql) will need to be downloaded manually.
    """
    engine = create_engine(conn_str, convert_unicode=True)
    engine.connect()

    set_conn(conn_string=conn_str)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
