"""Minimum Security Clearance Level for Graph Traversal

Find the smallest clearance level permitting travel from source to destination.
Input: n nodes numbered 0..n-1; directed edges (from_node, to_node, clearance).
A traveler with level C may use edges whose required clearance is <= C.
Output: the minimum nonnegative clearance, or None if no route exists.
Assumptions: source == destination requires clearance 0. Parallel edges and
cycles are allowed; endpoints are valid. Constraints: 1 <= n <= 10_000,
0 <= edges <= 100_000; clearance levels are nonnegative integers.
Examples:
    n=3, edges=[(0, 1, 4), (1, 2, 2), (0, 2, 7)], source=0, destination=2 -> 4.
    n=2, edges=[], source=0, destination=1 -> None.
Optional extension: each edge also carries a nonnegative travel cost. Among
routes permitted by the minimum necessary clearance, return minimum total cost
along with that clearance. No extension implementation is required.
"""

from __future__ import annotations

def minimum_clearance(n: int, edges: list[tuple[int, int, int]], source: int,
                      destination: int) -> int | None:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
