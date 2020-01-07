"""Console script for turbo-memory."""

import sys
import click


@click.command()
def turbo_memory(args=None):
    """Console script for turbo-memory."""
    # fmt: off
    click.echo("Replace this message by putting your code into "
               "turbo_memory.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    # fmt: on
    return 0


if __name__ == "__main__":
    sys.exit(turbo_memory)  # pragma: no cover