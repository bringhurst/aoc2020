from functools import reduce
from typing import Dict, List, Optional, Set

import click


@click.group()
def report_repair() -> None:
    "Day 1: Report Repair"


@report_repair.command()
def part_one_example() -> None:
    expense_report: List[int] = [1721, 979, 366, 299, 675, 1456]
    sum_to: int = 2020

    two_sum_results = calc_two_sum(expense_report, sum_to)
    result = reduce((lambda x, y: x * y), two_sum_results)

    print("Answer {}".format(result))


@report_repair.command()
def part_one_actual() -> None:
    expense_report: List[int] = [
        1619,
        1919,
        1441,
        1861,
        1932,
        1514,
        1847,
        1871,
        1764,
        1467,
        1970,
        1589,
        2009,
        1429,
        1098,
        1327,
        1502,
        1398,
        1710,
        1562,
        1512,
        1468,
        1762,
        1348,
        1356,
        1950,
        1266,
        1969,
        1815,
        1583,
        1959,
        1092,
        1694,
        1814,
        1763,
        1151,
        1981,
        1193,
        1614,
        1413,
        1642,
        1943,
        1407,
        895,
        1430,
        1706,
        1962,
        1522,
        1486,
        1986,
        1623,
        1489,
        1411,
        1851,
        1817,
        1416,
        1654,
        1438,
        1419,
        1649,
        1362,
        690,
        1804,
        1452,
        1766,
        1360,
        1807,
        1385,
        1964,
        1626,
        1832,
        745,
        1702,
        1602,
        1471,
        1996,
        1915,
        1813,
        1460,
        1925,
        1638,
        1581,
        1584,
        1379,
        1148,
        1554,
        1564,
        1914,
        1757,
        1820,
        1559,
        1096,
        1944,
        1587,
        1499,
        390,
        1733,
        1371,
        1781,
        2002,
        324,
        1655,
        1639,
        1482,
        1198,
        1264,
        1953,
        1320,
        1704,
        1321,
        1449,
        1455,
        1509,
        1765,
        1797,
        1703,
        1758,
        1610,
        1756,
        1901,
        1707,
        1968,
        1601,
        1328,
        1336,
        1592,
        1678,
        1699,
        1793,
        1957,
        2000,
        1306,
        1094,
        1545,
        1331,
        1751,
        1739,
        1335,
        1753,
        1983,
        1966,
        1934,
        1831,
        1426,
        1711,
        1840,
        1857,
        1347,
        1789,
        1409,
        1310,
        1752,
        1897,
        1497,
        1485,
        1125,
        1803,
        1577,
        919,
        1635,
        1791,
        1456,
        1796,
        1974,
        1954,
        1828,
        2004,
        1890,
        1376,
        1569,
        1406,
        1463,
        2006,
        1109,
        1620,
        1656,
        1870,
        1498,
        1645,
        1145,
        1681,
        1269,
        1527,
        1621,
        1575,
        1324,
        1647,
        1519,
        1697,
        1421,
        1216,
        1846,
        1625,
        1585,
        1369,
        1882,
        1823,
        1388,
        1548,
        1879,
    ]

    sum_to: int = 2020

    two_sum_results = calc_two_sum(expense_report, sum_to)
    result = reduce((lambda x, y: x * y), two_sum_results)

    print("Answer {}".format(result))


def calc_two_sum(inputs: List[int], sum_to: int) -> Set[int]:
    lookup: Dict[int, int] = dict()

    for i in inputs:
        lookup[sum_to - i] = i

    for i in inputs:
        j: Optional[int] = lookup.get(i)
        if not j:
            continue

        if i + j == sum_to:
            return set({i, j})

    raise ValueError("Two sum does not exist")


def calc_three_sum(inputs: List[int], sum_to: int) -> Set[int]:
    raise NotImplementedError()
