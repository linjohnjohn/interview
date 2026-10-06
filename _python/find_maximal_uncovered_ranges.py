"""Find Maximal Uncovered Ranges — LeetCode 2655

Return every maximal inclusive integer range not covered within domain [0,n-1].
Input: positive n and unsorted inclusive covered intervals [start,end], which
may overlap or repeat. Output: disjoint inclusive [start,end] uncovered ranges
in ascending order. A maximal range cannot be extended by even one domain integer
without reaching a covered point or leaving the domain. Endpoints of covered
intervals are covered; adjacent covered intervals leave no integer gap.
Constraints: 1 <= n <= 10^9; 0..100_000 intervals;
0 <= start <= end < n. Assumption: empty coverage is allowed.
Examples:
    n=10, ranges=[[3,5],[0,1],[7,7]] -> [[2,2],[6,6],[8,9]].
    n=3, ranges=[[0,2]] -> [].
"""

from __future__ import annotations

def find_maximal_uncovered_ranges(n: int, ranges: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
