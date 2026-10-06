"""Knapsack Variations

Core exercise: choose indivisible items maximizing total value without exceeding
capacity. Each item may be chosen at most once. Choosing no items is allowed.
Input: equal-length weights and values arrays plus an integer capacity.
Output: the maximum obtainable value; no selected-item list is required.
Assumptions: weights are positive integers; values are nonnegative integers.
Constraints: 0..100 items, 0 <= capacity <= 10_000, weights <= 10_000,
values <= 1_000_000.
Examples:
    weights=[2,3,4], values=[4,5,7], capacity=5 -> 9.
    weights=[2], values=[9], capacity=1 -> 0.
Optional variants (items remain indivisible and single-use):
    1. Restrict every value to 1 or 2; otherwise keep the core contract.
    2. Allow positive weights and nonnegative capacity with at most two decimal
       places, supplied as Decimal values with exact mathematical comparisons.
       Values remain integers. Example: weights=[Decimal('0.10'),Decimal('0.20')],
       values=[1,2], capacity=Decimal('0.30') -> 3.
Only the core signature is required; variant implementations are optional.
"""

from __future__ import annotations

def maximize_knapsack_value(weights: list[int], values: list[int], capacity: int) -> int:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
