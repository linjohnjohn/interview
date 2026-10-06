"""Find Root of N-Ary Tree — LeetCode 1506

Given an unordered collection of all node objects in a valid N-ary tree, return
the root object itself. Each node has a value and an ordered list of children.
Input: nodes, containing every node once; child references point to these objects.
Output: the existing root Node, not a copy or merely its value.
Constraints: 1..50_000 nodes; node values are distinct integers; the supplied
structure is a single valid tree. Node identity determines which object to return.
The Node constructor is provided only as a minimal input model.
Examples:
    a=Node(1), b=Node(2), c=Node(3); a.children=[b,c]; nodes=[c,a,b] -> a.
    a=Node(7); nodes=[a] -> a.
"""

from __future__ import annotations

from dataclasses import dataclass, field

@dataclass(eq=False)
class Node:
    val: int
    children: list[Node] = field(default_factory=list)


def find_root(nodes: list[Node]) -> Node:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
