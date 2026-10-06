"""Movie Recommendation System

Core exercise: recommend up to k movies related to one selected movie.
Input: movies maps unique string IDs to (genre_set, release_year), seed_id exists,
excluded_ids contains movies to omit, and k is nonnegative.
Score: 3 points per shared genre with the seed, plus 1 point if the release years
are within 5 years inclusive. Only candidates with a positive score qualify.
Exclude the seed and excluded_ids. Rank by score descending, then movie ID
lexicographically ascending. Output: ordered movie IDs, possibly fewer than k.
Assumptions: genre names are case-sensitive strings; excluded IDs absent from the
catalog are ignored. Constraints: 1..10_000 movies; <= 20 genres per movie;
1888 <= year <= 2100; 0 <= k <= 10_000.
Examples:
    movies={'a':({'drama'},2000), 'b':({'drama'},2003),
            'c':({'drama'},2010), 'd':({'comedy'},2001)},
    seed_id='a', excluded_ids=set(), k=3 -> ['b','c','d'] (scores 4,3,1).
    same movies, seed_id='a', excluded_ids={'b','c','d'}, k=3 -> [].
Optional personalized extension: accept a viewing-history set; exclude viewed
movies and rank candidates by the sum of their core pairwise scores against
history movies, using the same ID tie-break. Empty history produces no results.
"""

from __future__ import annotations

def recommend_movies(movies: dict[str, tuple[set[str], int]], seed_id: str,
                     excluded_ids: set[str], k: int) -> list[str]:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
