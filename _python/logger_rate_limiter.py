"""Logger Rate Limiter — LeetCode 359

Decide whether a message can be printed at a timestamp. Its first attempt is
allowed. Later attempts are allowed only if at least ten seconds have passed
since its previous successful print. Rejected attempts do not reset the cooldown.
Input: sequential shouldPrintMessage(timestamp, message) calls; timestamps are
nonnegative integer seconds in nondecreasing order. Output: boolean per call.
Constraints: at most 100_000 calls; 1 <= message length <= 100; timestamp <= 10^9.
Examples:
    (1,'foo'), (2,'foo'), (10,'foo'), (11,'foo') -> True,False,False,True.
    (0,'a'), (0,'b'), (10,'a') -> True,True,True.
"""

from __future__ import annotations

class Logger:
    def __init__(self) -> None:
        raise NotImplementedError

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
