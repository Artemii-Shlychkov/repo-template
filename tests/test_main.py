import pytest

from src.my_package import main as mut


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ],
)
def test_main(a: int, b: int, expected: int) -> None:
    result = mut.main(a, b)
    assert result == expected, (
        f"Expected {expected}, but got {result} for inputs {a} and {b}"
    )
