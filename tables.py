import logging
from textwrap import wrap
import sys

logger = logging.getLogger(__name__)


class Field:
    def __init__(self, name, align='left'):
        self.name = name
        self.align = align
        self.value = None

    def __iter__(self, width):
        return FieldIter(self, width)

    def __repr__(self):
        return '<Field "%s">' % self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class FieldIter:
    def __init__(self, field, width):
        self.field = field
        self.width = width
        self.data = None

    def __next__(self):
        return

    def __repr__(self):
        return '<Cell "%s">' % self.field.name

    def __str__(self):
        return ''

    def readline(self, width):
        pass


class Table:
    styles = {'ascii': '-|+',
              }
    def __init__(self, width=80, height=None, padding=1, title=None):
        self.width = width
        self.height = height
        self.padding = padding
        self.title = title

        self.cells = [[Cell(Field(None), 0, 0)]]

        self.fields = []

    def __repr__(self):
        pass

    @property
    def rows(self):
        return len(self.cells)

    @property
    def cols(self):
        return len(self.cells[0])

    def expand(self, num_rows, num_cols):
        for row in range(num_rows):
            try:
                self.cells[row]
            except IndexError:
                self.cells.append([])

            for col in range(num_cols):
                try:
                    self.cells[row][col]
                except IndexError:
                    self.cells[row].append(None)

    def trim(self):
        max_row = 0
        max_col = 0

        for row in range(self.rows):
            for col in range(self.cols):
                cell = col
                if cell is not None:
                    if max_row < row:
                        max_row = row
                    if max_col < col:
                        max_col = col

        self.cells = [[self.cells[row][col] for col in range(max_col)] for row in range(max_row)]

    def add_field(self, field, row_a, col_a, row_b=None, col_b=None):
        self.fields.append(field)

    def set_row_height_share(self, shares):
        pass

    def set_col_width_share(self, shares):
        pass

    def render(self, data):
        cells_filled = []
        for row in range(self.rows):
            row = []
            for col in range(self.cols):
                row.append(iter(col))
            cells_filled.append(row)




        for key, value in data.items():
            for field in self.fields:
                if key == field.name:
                    field.value = value



if __name__ == '__main__':
    field_name = Field('name', width=20)
    table = Table()
    table.resize(3,5)
    table.debug()
