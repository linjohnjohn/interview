"""Car Rental Optimization

Assign every rental request to a car while minimizing the number of cars used.
Input: requests are (request_id, pickup_time, return_time) tuples in any order.
Output: (assignments, car_count), where assignments maps every request ID to a
car ID. Car IDs are integers 0..car_count-1. Any optimal assignment is accepted.
Assumptions: IDs are unique strings, times are integers, pickup < return,
and requests occupy [pickup, return). A return and pickup at the same time may
share a car. Cars are identical; there are no travel or cleaning delays.
Constraints: 0 <= number of requests <= 100_000; times are nonnegative.
Examples:
    [('a', 0, 3), ('b', 2, 4), ('c', 3, 5)]
    -> ({'a': 0, 'b': 1, 'c': 0}, 2), one accepted assignment.
    [] -> ({}, 0).
"""

from __future__ import annotations

def assign_cars(requests: list[tuple[str, int, int]]) -> tuple[dict[str, int], int]:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
