"""Command line interface for microkg."""
import click


@click.group()
def microkg_cli():
    """PoC"""
    pass


@microkg_cli.command()
def parse():
    """Parse"""
    from . import parser

    parser.main()


@microkg_cli.command()
def release():
    """Release"""
    from . import releaser

    releaser.main()


if __name__ == "__main__":
    microkg_cli()
