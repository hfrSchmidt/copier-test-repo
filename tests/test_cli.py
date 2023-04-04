#!/usr/bin/env python

"""Tests for the `hfrschmidt_test_project` CLI."""

from click.testing import CliRunner

from hfrschmidt_test_project import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "hfrschmidt_test_project.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output


def test_cli_option_abcd_str_input():
    runner = CliRunner()

    result = runner.invoke(cli.main, ["-a", "dummy"])
    assert result.exit_code == 0
    assert "Your option: dummy" in result.output

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "-a, --abcd TEXT" in help_result.output


def test_cli_option_abcd_empty_str_input():
    runner = CliRunner()

    result = runner.invoke(cli.main, ["-a", ""])
    assert result.exit_code == 0
    assert "hfrschmidt_test_project.cli.main" in result.output


def test_cli_option_abcd_no_input():
    runner = CliRunner()

    result = runner.invoke(cli.main, ["-a"])
    assert result.exit_code == 2
    assert "Error: Option '-a' requires an argument." in result.output
