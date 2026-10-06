"""Request Rate Limiter

Implement a per-client limiter accepting at most limit requests in a rolling
window of window_seconds seconds. allow(client_id, timestamp) returns whether
this request is accepted. Only accepted requests count toward later limits.
Window boundary: for a request at t, count earlier accepted timestamps s with
 t-window_seconds < s <= t. An accepted request exactly window_seconds ago has
expired. Include the current request when deciding whether the limit is exceeded.
Assumptions: calls are sequential, timestamps are nonnegative integer seconds
in globally nondecreasing order, clients are independent, and equal timestamps
are allowed. Constraints: limit >= 1, window_seconds >= 1; <= 100_000 calls.
Examples:
    limit=2, window_seconds=10; calls ('a',0),('a',1),('a',9),('a',10)
    -> True,True,False,True.
    limit=1, window_seconds=5; ('a',0),('b',0),('a',0) -> True,True,False.
Optional extension: define and implement behavior under concurrent requests.
"""

from __future__ import annotations

class RequestRateLimiter:
    def __init__(self, limit: int, window_seconds: int) -> None:
        raise NotImplementedError

    def allow(self, client_id: str, timestamp: int) -> bool:
        raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
