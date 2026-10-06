"""Chunk Upload Acknowledgment Tracker

Track acknowledgments for chunks numbered 0 through n-1.
ack(chunkId) records an acknowledgment; repeats have no additional effect.
getUploadedPrefix() returns the length of the acknowledged prefix starting at
zero, not the total acknowledgment count. It returns n when all chunks are
acknowledged. An empty tracker always returns zero.
Input: initialization integer 0 <= n <= 1_000_000; ack receives only valid integer
IDs, in any order. Calls are sequential. Output: ack returns None; prefix queries
return an integer in 0..n. No invalid-ID behavior needs implementation.
Examples:
    n=5; ack IDs 2,0,1,4,3; query after each -> 0,1,3,3,5.
    n=3; ack(0), ack(0); getUploadedPrefix() -> 1.
Optional extension: initialize a finite range [start, start+n) and query the
smallest unacknowledged chunk number, returning start+n when all are acknowledged.
"""

from __future__ import annotations

class ChunkUploadAcknowledgmentTracker:
    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def ack(self, chunkId: int) -> None:
        raise NotImplementedError

    def getUploadedPrefix(self) -> int:
        raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
