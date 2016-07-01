import unittest
from cli.tables import *


class TestField(unittest.TestCase):
    def setUp(self):
        self.name = 'testfield'
        self.field = Field(self.name)

    def test_str__(self):
        self.assertEqual(str(self.field), self.name[0:8])


class TestTable(unittest.TestCase):
    def setUp(self):
        started = [[None, None, None, None],
                   [None, None, None, None],
                   [None, None, None, None],
                   [None, None, 1234, None],
                   [None, None, None, None]]

        self.table = Table()
        self.table.cells = started

    def test_rows(self):
        self.assertEqual(self.table.rows, 5)

    def test_cols(self):
        self.assertEqual(self.table.cols, 4)

    def test_expand(self):
        self.table.cells[4][3] = 4321
        expected = [[None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, None, None, None],
                    [None, None, 1234, None, None],
                    [None, None, None, 4321, None],
                    [None, None, None, None, None]]

        self.table.expand(6, 5)
        self.assertListEqual(self.table.cells, expected)

    def test_trim(self):
        expected = [[None, None, None],
                    [None, None, None],
                    [None, None, None],
                    [None, None, 1234]]

        self.table.trim()
        self.assertListEqual(self.table.cells, expected)

    def test_add_field(self):
        field = Field('test', rowspan=2)

        expected = [[None, None, None, None],
                    [None, None, None, None],
                    [None, None, None, None],
                    [None, None, 1234, None],
                    [None, None, None, None]]

        self.table.add_field(field, 1, 1)
        self.fail()


@unittest.skip
class TestTableAPI(unittest.TestCase):
    def test_usage(self):




if __name__ == '__main__':
    unittest.main()
