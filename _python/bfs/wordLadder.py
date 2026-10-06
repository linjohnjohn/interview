from collections import defaultdict

LETTER_TO_INT = {} 
a = ord("a")
for l in "abcdefghijklmnopqrstuvwxyz":
    LETTER_TO_INT[l] = ord(l) - a
    LETTER_TO_INT["*"] = 26
class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordlist: list[str]) -> int:
        # put words in word list in a map or set: O(n)
        # for each word in word list, mutate every character in every position and see if it matches with other words
        # if it does then create an edge between them: O(n * m ^ 2) since only 26 possible characters in each position
        # this creates O(nm) edges too
        # run bfs to see if begin word can reach end word: O(nm + n)

        # for each word in list, create an intermediate wildcard node for every character in the word and connect an edge to them: hot -> *ot h*t ho*: O(nm^2)
        # and O(nm) edges. We can reduce runtime to O(nm) by representing word as a number so they are mutable

        adj = defaultdict(list)
        if endWord not in wordlist:
            return 0

        if beginWord not in wordlist:
            wordlist.append(beginWord)

        for word in wordlist:
            wordNum = self.word_to_num(word)

            for idx, l in enumerate(word):
                base = 27 ** idx
                wildcard = wordNum - (LETTER_TO_INT[l] + LETTER_TO_INT["*"]) * base
                adj[wordNum].append(wildcard)
                adj[wildcard].append(wordNum)

        return self.bfs(adj, self.word_to_num(beginWord), self.word_to_num(endWord)) // 2
    

    def bfs(self, adj: dict[int, list[int]], start: int, end: int):
        visited = set()
        hops = 2
        level = [start]

        while level:
            newLevel = []
            for n in level:
                if n == end:
                    return hops
                if n not in visited:
                    visited.add(n)
                    newLevel.extend(adj[n])
            
            level = newLevel
            hops += 1
        
        return 0

    # converts a word to number treating each character as a base 27 digit, where the left most character is the smallest digit
    def word_to_num(self, word: str):
        n = 0
        for l in reversed(word):
            n *= 27
            n += LETTER_TO_INT[l]
        return n
    

s = Solution()
wordlist = ['cat', 'cad', 'sad', 'sat', 'sud', 'bud']
print(s.ladderLength('cat', 'sad', wordlist))
print(s.ladderLength('cat', 'sat', wordlist))
print(s.ladderLength('cat', 'bud', wordlist))
print(s.ladderLength('cat', 'lid', wordlist))
print(s.ladderLength('hat', 'bud', wordlist))
