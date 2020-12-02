from aoc2020.commands import password_philosophy


def test_parse_password_input():
    mock_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

    mock_passwd_one = password_philosophy.Password(
        password_value="abcde",
        letter="a",
        letter_low_limit=1,
        letter_high_limit=3,
    )

    mock_passwd_two = password_philosophy.Password(
        password_value="cdefg",
        letter="b",
        letter_low_limit=1,
        letter_high_limit=3,
    )

    mock_passwd_three = password_philosophy.Password(
        password_value="ccccccccc",
        letter="c",
        letter_low_limit=2,
        letter_high_limit=9,
    )

    results = password_philosophy.parse_password_input(mock_input)

    assert mock_passwd_one in results
    assert mock_passwd_two in results
    assert mock_passwd_three in results
