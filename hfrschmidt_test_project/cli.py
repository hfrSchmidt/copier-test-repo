"""Console script for hfrschmidt_test_project."""
import sys

import click


@click.command()
@click.option("-a", "--abcd", type=str)
def main(abcd, args=None):
    """Console script for hfrschmidt_test_project."""

    if abcd != "" and abcd is not None:
        click.echo(f"Your option: { abcd }")
        return 0

    click.echo("Place your code into hfrschmidt_test_project.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
