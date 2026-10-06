"""Design Add and Search Words — LeetCode 211

Support adding words and searching for a pattern matching any added word.
In a search pattern, '.' matches exactly one lowercase letter. Other characters
match literally. A search must match the entire word, not just a prefix.
Input: addWord(word) and search(pattern). Output: add returns None; search boolean.
Constraints: words have 1..25 lowercase English letters; patterns have 1..25
lowercase letters/dots; <= 10_000 calls. Duplicate additions have no extra effect.
Examples:
    addWord('bad'), addWord('dad'), addWord('mad');
    search('pad') -> False; search('bad') -> True; search('.ad') -> True.
    addWord('a'); search('..') -> False.
"""

from __future__ import annotations

class WordDictionary:
    def __init__(self) -> None:
        raise NotImplementedError

    def addWord(self, word: str) -> None:
        raise NotImplementedError

    def search(self, pattern: str) -> bool:
        raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
