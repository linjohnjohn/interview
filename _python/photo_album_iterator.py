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
        self.album = album
        self.favourites = favourites
        self.N = len(album)        

        if (len(favourites) == 0):
            self.fav_index = self.N
        else:
            self.fav_index = self._find_next(-1, True)
        self.nor_index = self._find_next(-1, False)
        
    def _find_next(self, index, is_favorite):
        '''Given an starting index, finds next valid index of photo type
        Args:
            index: starting index (non-inclusive, search will start after this)
            is_favorite: whether to find next valid favorite or normal photo

        Returns:
            if exists: next valid index for photo type
            else: len of album (out of bound index)
        '''
        i = index + 1
        while i < self.N:
            is_valid = self.album[i] in self.favourites if is_favorite else self.album[i] not in self.favourites
            if is_valid:
                return i
            i += 1
        return self.N
        

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.fav_index < self.N:
            nxt = self.album[self.fav_index]
            self.fav_index = self._find_next(self.fav_index, True)
            return nxt
        elif self.nor_index < self.N:
            nxt = self.album[self.nor_index]
            self.nor_index = self._find_next(self.nor_index, False)
            return nxt
        raise StopIteration


album = ['A', 'B', 'C', 'D']
fav = set(['B', 'D'])
it = PhotoAlbumIterator(album, fav)
print(list(it))

album = []
fav = set()
it = PhotoAlbumIterator(album, fav)
print(list(it))

album = ['A', 'B', 'C', 'D']
fav = set()
it = PhotoAlbumIterator(album, fav)
print(list(it))

"""
# Approach / invariant
- two pointers, favoriteIndex, normalIndex each initialized to index of first favorite or normal photo
- next will return next valid photo from fav_index first then nor_index and also precompute the corresponding next valid index

# Complexity
"""

