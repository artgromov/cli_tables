# Small library to create cli tables with simple to use API
## Overview
**Work in progress...**

Desired to be an extension for my cli framework.

Key differences from other cli table modules:
- user-friendly
- form/template like usage

## Partial example
```python
table = Table(width=50, height=20, padding=0, title='title')

field1 = Field(name='field1', align='center')
field2 = Field(name='field2')
field3 = Field(name='field3')
field4 = Field(name='field4')

table.add_field(field1, 0, 0, 0, 1)
table.add_field(field2, 1, 0, 2, 0)
table.add_field(field3, 1, 1, 2, 2)
table.add_field(field4, 0, 2)

table.set_row_height_share([5, 2, 2])
table.set_col_width_share([3, 3, 3])
```
