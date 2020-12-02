import re
from dataclasses import dataclass
from typing import Set

import click


@click.group()
def password_philosophy() -> None:
    "Day 2: Password Philosophy"


@dataclass(frozen=True)
class Password:
    password_value: str
    letter: str
    letter_low_limit: int
    letter_high_limit: int


def parse_password_input(passwd_input: str) -> Set[Password]:
    prog = re.compile(r"(\d+)-(\d+) (.+): (.+)")
    results: Set[Password] = set()

    for line in passwd_input.splitlines():
        match = prog.match(line)
        if not match:
            continue

        (letter_low_limit, letter_high_limit, letter, password_value) = match.groups()

        results.add(
            Password(
                password_value=password_value,
                letter=letter,
                letter_low_limit=int(letter_low_limit),
                letter_high_limit=int(letter_high_limit),
            )
        )

    return results


@password_philosophy.command()
def part_one_example() -> None:
    print("example output")


@password_philosophy.command()
def part_one_actual() -> None:
    print("actual output")
