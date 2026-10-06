"""Split String by Spaces Outside Quotes

Split text on ordinary spaces outside balanced single quotes. Keep the quotes
and all spaces inside them. Consecutive separating spaces create no empty tokens.
Quoted and unquoted text may be adjacent within one token.
Input: a string with balanced single quotes, no literal apostrophes, and no
escaped quotes. Output: a list of tokens retaining their original text.
Assumptions: only ASCII space ' ' separates tokens; tabs and newlines are ordinary
characters. Constraints: 0 <= text length <= 100_000. Empty/all-space input -> [].
Examples:
    "say 'hello world'now" -> ["say", "'hello world'now"].
    "  a  '' b  " -> ['a', "''", 'b'].
"""

from __future__ import annotations

def split_outside_quotes(text: str) -> list[str]:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
