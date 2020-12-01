import click


@click.group()
def report_repair() -> None:
    "Day 1: Report Repair"
    pass


@report_repair.command("foo")
def report_repair_foo() -> None:
    print("foo cmd here")
