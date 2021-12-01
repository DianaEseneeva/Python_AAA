from typing import List, Tuple
import unittest
from unittest import TestCase


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


class Test(TestCase):
    def test_output(self):
        test1 = ['Moscow', 'New York', 'Moscow', 'London']
        test2 = ['Hello', 'How', 'Are', 'You', 'Doing']
        test3 = ['hi', 'hello', 'hello', 'hello', 'hi', 'cats']
        test4 = ['New Year', 'New Year Eve', 'Christmas']
        output1 = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        output2 = [('Hello', [0, 0, 0, 0, 1]),
                   ('How', [0, 0, 0, 1, 0]),
                   ('Are', [0, 0, 1, 0, 0]),
                   ('You', [0, 1, 0, 0, 0]),
                   ('Doing', [1, 0, 0, 0, 0])]
        output3 = [('hi', [0, 0, 1]),
                   ('hello', [0, 1, 0]),
                   ('hello', [0, 1, 0]),
                   ('hello', [0, 1, 0]),
                   ('hi', [0, 0, 1]),
                   ('cats', [1, 0, 0])]
        output4 = [('New Year', [0, 0, 1]), ('New Year Eve', [0, 1, 0]), ('Christmas', [1, 0, 0])]
        self.assertEqual(fit_transform(test1), output1)
        self.assertEqual(fit_transform(test2), output2)
        self.assertEqual(fit_transform(test3), output3)
        self.assertEqual(fit_transform(test4), output4)

    def test_exception(self):
        with self.assertRaises(TypeError) as msg1:
            fit_transform()
        self.assertTrue('expected at least 1 arguments, got 0' in str(msg1.exception))

        with self.assertRaises(TypeError) as msg2:
            fit_transform(1, 2, 3)
        self.assertFalse('expected at least 1 arguments, got 0' in str(msg2.exception))


if __name__ == '__main__':
    unittest.main()
