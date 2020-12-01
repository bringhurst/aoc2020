import click

from aoc2020.commands.report_repair import report_repair


@click.group()
def main() -> None:
    "Advent of Code 2020"
    pass


main.add_command(report_repair)
