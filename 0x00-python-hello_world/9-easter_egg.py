#!/usr/bin/python3
import this
import textwrap
zen_python = "".join(this.d.get(c, c) for c in this.s)
limit = textwrap.fill(zen_python, width=98)
print(limit)
