"""String Template Substitution with Nested Variables and Cycle Detection

Replace each %name% placeholder in text with its mapping value, fully expanding
placeholders inside that value. Return the expanded string.
Input: text and a mapping from variable names to string values.
Assumptions: variable names are nonempty ASCII letters, digits, or underscores.
All percent signs belong to well-formed placeholders; escaping is not supported.
Unknown variables encountered during expansion raise KeyError with their name.
A cyclic dependency encountered during expansion raises ValueError. Unreferenced
mapping entries, including cycles, do not affect the result. Repeated references
to a variable alone are not a cycle. Empty values are allowed.
Constraints: at most 1_000 variables; total input and valid expanded output each
at most 100_000 characters. No truncation behavior is required.
Examples:
    text='Hi %greeting%', variables={'greeting':'%name%!', 'name':'Ada'} -> 'Hi Ada!'.
    text='%a%', variables={'a':'%b%', 'b':'%a%'} -> raises ValueError.
"""

from __future__ import annotations

def substitute_template(text: str, variables: dict[str, str]) -> str:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
