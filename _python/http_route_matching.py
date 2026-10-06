"""HTTP Route Matching

Register route patterns and retrieve the handler for a matching path.
Patterns contain literal segments or a whole-segment placeholder such as {id}.
Each placeholder matches exactly one nonempty segment; segment counts must match.
Input: registerHandler(pattern, handler), then getHandler(path).
Output: register returns None; lookup returns the handler string or None if no match.
Assumptions: handlers are string identifiers. Paths/patterns begin with '/', have
no trailing slash except root '/', and no empty internal segments. Matching is
case-sensitive, with no query strings, percent decoding, or HTTP method handling.
Parameter names are nonempty letters/underscores and unique within a pattern.
Precedence: more literal segments wins; equal counts use earliest registration.
Registering an identical pattern replaces its handler without changing its order.
Constraints: <= 10_000 registrations/lookups; <= 20 segments per route.
Examples:
    register('/users/{id}','user'); register('/users/me','self');
    get('/users/me') -> 'self'; get('/users/7') -> 'user'.
    register('/{x}/details','first'); register('/users/{id}','second');
    get('/users/details') -> 'first'; get('/missing') -> None.
"""

from __future__ import annotations

class HTTPRouteMatcher:
    def __init__(self) -> None:
        raise NotImplementedError

    def registerHandler(self, pattern: str, handler: str) -> None:
        raise NotImplementedError

    def getHandler(self, path: str) -> str | None:
        raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
