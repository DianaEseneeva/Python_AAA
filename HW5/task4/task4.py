from typing import List, Tuple
import pytest


def fit_transform(*args: List[str]) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


@pytest.mark.parametrize('test, output', [
    (['Moscow', 'New York', 'Moscow', 'London'], [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]),
        (['Hello', 'How', 'Are', 'You', 'Doing'], [('Hello', [0, 0, 0, 0, 1]),
                   ('How', [0, 0, 0, 1, 0]),
                   ('Are', [0, 0, 1, 0, 0]),
                   ('You', [0, 1, 0, 0, 0]),
                   ('Doing', [1, 0, 0, 0, 0])]),
    (['hi', 'hello', 'hello', 'hello', 'hi', 'cats'], [('hi', [0, 0, 1]),
                   ('hello', [0, 1, 0]),
                   ('hello', [0, 1, 0]),
                   ('hello', [0, 1, 0]),
                   ('hi', [0, 0, 1]),
                   ('cats', [1, 0, 0])]),
    (['New Year', 'New Year Eve', 'Christmas'], [('New Year', [0, 0, 1]),
                                                 ('New Year Eve', [0, 1, 0]),
                                                 ('Christmas', [1, 0, 0])])
])
def test_output(test, output):
    assert fit_transform(test) == output


def test_exception():
    with pytest.raises(TypeError) as msg:
        fit_transform()
    assert str(msg.value) == 'expected at least 1 arguments, got 0'
    with pytest.raises(TypeError):
        fit_transform(1, 2, 3)

