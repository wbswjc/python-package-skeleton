import pytest


@pytest.mark.parametrize(('a', 'b', 'output'), (
        (0, 1, 1),
        (1, 2, 3),
))
def test_display_microseconds(a, b, output):
    assert output == a + b
