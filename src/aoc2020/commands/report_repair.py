from typing import Dict, List, Set

import click


@click.group()
def report_repair() -> None:
    "Day 1: Report Repair"
    pass


@report_repair.command("foo")
def report_repair_foo() -> None:
    print("foo cmd here")


def calc_two_sum(inputs: List[int], sum_to: int) -> Set[int]:
    lookup: Dict[int, int] = dict()

    for i in inputs:
        lookup[sum_to - i] = i

    for i in inputs:
        j = lookup[i]
        if i + j == sum_to:
            return set({i, j})

    raise ValueError("Two sum does not exist")
