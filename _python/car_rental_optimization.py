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
import heapq

def assign_cars(requests: list[tuple[str, int, int]]) -> tuple[dict[str, int], int]:
    sorted_request = requests.copy()
    sorted_request.sort(key=lambda req: req[1])
    # min-heap with (endtime, car_id)
    soonest_heap = []
    car_count = 0
    assignments = {}

    for req in sorted_request:
        request_id, start, end = req
        top = soonest_heap[0] if len(soonest_heap) > 0 else None
        if top == None or top[0] > start:
            heapq.heappush(soonest_heap, (end, car_count))
            assignments[request_id] = car_count
            car_count += 1
        else:
            soonest_end, car_id = top
            heapq.heapreplace(soonest_heap, (end, car_id))
            assignments[request_id] = car_id

    return (assignments, car_count)



req = [('a', 0, 1), ('b', 1, 3)]
print(assign_cars(req))

req = [('a', 0, 1)]
print(assign_cars(req))

req = [('a', 0, 4), ('b', 2, 5), ('c', 3, 5), ('d', 5, 6)]
print(assign_cars(req))


"""
Approach / invariant
- sort requests by start_time then a min-heap of earliest return times keeps track of earliest car we can reuse and total number of cards needed
- at any point if start_time < top_of_heap, then the current request must overlap with all outstanding rentals at start_time because 
start_outstanding <= start_time (based on sorted processing order) and top_of_heap <= end_outstanding (by heap property) which implies start_outstanding <= start_time < top_of_heap <= end_outstanding 

Complexity
n = number of requests, C = cars needed, n >= C
time: O(n logn) for sort, O(n log C) for determining optimal assignment
space O(C) for heap, O(n) for assignment dictionary
"""
