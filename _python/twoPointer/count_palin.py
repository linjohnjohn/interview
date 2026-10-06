# Problem: Palindromic Substrings
# Count contiguous substrings that read the same forward and backward. Identical text at
# different positions counts separately.
#
# Expected input/output: s='abc' -> 3; s='aaa' -> 6; s='' -> 0

class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointers approach
        # at every character and empty space between character
        # check if it's a valid palin and add it to results, then expand l, r pointers outwards
        # and keep checking

        # O(n) characters and empty spaces, each expansion results in O(n) operations, O(1) space for pointers
        
        def matches(l: int, r: int) -> bool:
            # bound check
            if l < 0 or r >= len(s):
                return False
            
            if s[l] == s[r]:
                return True
            else:
                return False


        count = 0
        for i in range(len(s)):
            # odd length case
            l, r = i, i
            while matches(l, r):
                l -= 1
                r += 1
                count += 1
            
            l, r = i, i + 1
            while matches(l, r):
                l -= 1
                r += 1
                count += 1

        return count
    

s = Solution()
print(s.countSubstrings('aaa'))
print(s.countSubstrings('abc'))
print(s.countSubstrings('hannah'))

# Key insight:
# Every palindrome has a center at a character or between two characters. Expand outward from
# both kinds of center while the ends match.
