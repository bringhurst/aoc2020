import click


@click.group()
def command_template() -> None:
    "Day 999: Command Template"


@command_template.command()
def part_one_example() -> None:
    print("example output")


@command_template.command()
def part_one_actual() -> None:
    print("actual output")
