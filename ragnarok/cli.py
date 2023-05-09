"""Console script for ragnarok."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for ragnarok."""
    click.echo("Replace this message by putting your code into "
               "ragnarok.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    click.echo("If you can see this message, then that means things are working.")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
