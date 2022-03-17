from general_code.diff_code.diff_files import generate_diff


def test_diff_files():
    assert generate_diff(2) == 4
