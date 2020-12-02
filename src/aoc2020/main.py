import click

from aoc2020.commands.command_template import command_template
from aoc2020.commands.password_philosophy import password_philosophy
from aoc2020.commands.report_repair import report_repair


@click.group()
def main() -> None:
    "Advent of Code 2020"
    pass


main.add_command(command_template)
main.add_command(report_repair)
main.add_command(password_philosophy)
