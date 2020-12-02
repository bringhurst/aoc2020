import click


@click.group()
def password_philosophy() -> None:
    "Day 2: Password Philosophy"


@password_philosophy.command()
def part_one_example() -> None:
    print("example output")


@password_philosophy.command()
def part_one_actual() -> None:
    print("actual output")
