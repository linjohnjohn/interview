"""Count Closed Lakes / Number of Closed Islands — LeetCode 1254

Count four-directionally connected water regions that do not touch any boundary.
Use 'L'=land and 'W'=water. If any cell in a water region lies on the first/last
row or first/last column, exclude the entire region. Diagonal contact does not
connect regions. This L/W variant is one problem, distinct from Count Lakes,
which includes boundary-connected regions.
Input: a valid rectangular character grid. Output: number of closed water regions.
Constraints: up to 500 rows and 500 columns, only L/W; mutation is allowed.
Empty grids and zero-column grids return zero.
Examples:
    grid=[['L','L','L'],['L','W','L'],['L','L','L']] -> 1.
    grid=[['L','W','L'],['L','W','L'],['L','L','L']] -> 0.
"""

from __future__ import annotations

def count_closed_lakes(grid: list[list[str]]) -> int:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
