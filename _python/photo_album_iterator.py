"""Photo Album Iterator with Favourites First

Provide an iterator yielding favourite photos first, then non-favourites.
Preserve original album order within each group and emit each photo exactly once.
Input: album is an ordered list of unique string photo IDs; favourites is a set
of IDs. Output: each next() yields one ID; exhausted iterators raise StopIteration.
Assumptions: favourite IDs absent from the album are ignored; the album and
favourites are not modified after construction. Constraints: 0..100_000 photos.
Examples:
    album=['p1', 'p2', 'p3', 'p4'], favourites={'p2', 'p4'}
    -> iterator output ['p2', 'p4', 'p1', 'p3'].
    album=[], favourites={'missing'} -> iterator output [].
"""

from __future__ import annotations

from typing import Iterator

class PhotoAlbumIterator(Iterator[str]):
    def __init__(self, album: list[str], favourites: set[str]) -> None:
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        raise NotImplementedError

    def __next__(self) -> str:
        raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
