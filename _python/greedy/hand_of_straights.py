from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # let's sort the hand first, or put onto freq table and sort
        # then starting from the lowest card, let's try to create straights
        # if its not possible to create a straight with the lowest card, then
        # it must not be possible to complete the problem
        freq = defaultdict(int)

        for i in hand:
            freq[i] += 1

        keys = list(freq.keys())
        keys.sort()

        for card in keys:
            while freq[card] > 0:
                for i in range(groupSize):
                    if freq[card + i] == 0:
                        return False
                    freq[card + i] -= 1

        return True


s = Solution()
# hand = [1, 2, 4, 2, 3, 5, 3, 4]
# groupSize = 4
# print(s.isNStraightHand(hand, groupSize))

# hand = [1, 2, 3, 3, 4, 5, 6, 7]
# groupSize = 4
# print(s.isNStraightHand(hand, groupSize))
hand = [1, 1, 2, 2, 3, 3]
groupSize = 3
print(s.isNStraightHand(hand, groupSize))
