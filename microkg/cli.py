"""Command line interface for microkg."""
import click


@click.group()
def microkg_cli():
    """PoC"""
    pass


@microkg_cli.command()
def info():
    """Show some info."""
    from . import parser

    parser.main()


if __name__ == "__main__":
    microkg_cli()
