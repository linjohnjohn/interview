"""Friend Recommendations

Recommend up to k new friends from a social graph, ranking by number of mutual
friends descending, then candidate ID ascending for ties.
Input: graph maps each integer user ID to the set of their friends; user and k.
Output: ordered candidate IDs, excluding the user and existing friends.
Assumptions: friendships are undirected and symmetric; all users appear as keys,
there are no self-friendships, user exists, and only candidates with at least one
mutual friend qualify. If fewer than k qualify, return all qualifying candidates.
Constraints: 1..10_000 users, 0..100_000 undirected friendships, 0 <= k <= 10_000.
This is a custom social-graph exercise, not the SQL task LeetCode 1917.
Examples:
    graph={1:{2,3}, 2:{1,4}, 3:{1,4,5}, 4:{2,3}, 5:{3}}, user=1, k=2 -> [4,5].
    graph={1:{2}, 2:{1}}, user=1, k=3 -> [].
"""

from __future__ import annotations

def recommend_friends(graph: dict[int, set[int]], user: int, k: int) -> list[int]:
    raise NotImplementedError


# TODO: Clarifying questions
#

# TODO: Approach / invariant
#

# TODO: Complexity
#

# TODO: Edge cases
#
