"""Console script for hfrschmidt_test_project."""
import sys

import click


@click.command()
def main(args=None):
    """Console script for hfrschmidt_test_project."""
    click.echo("Place your code into hfrschmidt_test_project.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
