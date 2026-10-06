"""Multi-Pattern String Replacement

Replace whole whitespace-delimited tokens using a supplied string mapping.
Input: text and replacements. Output: text with matching tokens replaced while
preserving every original whitespace character exactly.
Assumptions: delimiters are ASCII space, tab, newline, carriage return, form feed,
and vertical tab. Keys are nonempty tokens with no delimiters. Matching is
case-sensitive; punctuation belongs to the token and is not stripped. Thus 'cat,'
does not match 'cat'. Replacement values may contain whitespace or be empty.
Replacement text is emitted once and never processed for further replacements.
Constraints: text and total mapping text each <= 100_000 characters.
Examples:
    text='cat  cat, Cat', replacements={'cat':'dog'} -> 'dog  cat, Cat'.
    text='a b', replacements={'a':'b', 'b':'c'} -> 'b c'.
"""

from __future__ import annotations

def replace_words(text: str, replacements: dict[str, str]) -> str:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
