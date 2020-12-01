from typing import List, Set

from aoc2020.commands import report_repair


def test_two_sum():
    mock_input: List[int] = [1721, 979, 366, 299, 675, 1456]
    mock_sum_to: int = 2020
    mock_result: Set[int] = {1721, 299}

    assert report_repair.calc_two_sum(mock_input, mock_sum_to) == mock_result


def test_three_sum():
    mock_input: List[int] = [1721, 979, 366, 299, 675, 1456]
    mock_sum_to: int = 2020
    mock_result: Set[int] = {979, 366, 675}

    assert report_repair.calc_three_sum(mock_input, mock_sum_to) == mock_result


