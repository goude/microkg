"""Command line interface for microkg.  """
import click


@click.group()
def microkg_cli():
    """PoC"""
    pass


@microkg_cli.command()
def info():
    """Show some info."""
    click.echo("Here's your info. Thank you for your coöperation.")


if __name__ == "__main__":
    microkg_cli()
