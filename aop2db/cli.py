"""Console script for aop2db."""
import sys
import click
import logging

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


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
