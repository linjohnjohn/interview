from __future__ import annotations

class PrefixTree:

    def __init__(self):
        self.has_word = False
        self.word = None
        self.children = {}

    def insert(self, word: str, index = 0) -> None:
        if (index == len(word)):
            self.has_word = True
            self.word = word
            return

        char = word[index]
        if (char not in self.children):
            self.children[char] = PrefixTree()
        self.children[char].insert(word, index + 1)
        
    def get_subtrie(self, char) -> PrefixTree:
        if (char not in self.children):
            return None
        else:
            return self.children[char]

    def search(self, word: str, index = 0) -> bool:
        if (len(word) == index):
            return self.has_word

        char = word[index]
        if (char not in self.children):
            return False
        else:
            return self.children[char].search(word, index + 1)        
        

    def startsWith(self, prefix: str, index = 0) -> bool:
        if (index == len(prefix)):
            return True

        char = prefix[index]
        if (char not in self.children):
            return False
        else:
            return self.children[char].startsWith(prefix, index + 1)
        

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ROWS, COLS = len(board), len(board[0])
        prefixTree = PrefixTree()
        for w in words:
            prefixTree.insert(w)
        output = set()
        board_visited = set()
        def dfs(i: int, j: int, trie: PrefixTree):
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or (i, j) in board_visited:
                return

            board_visited.add((i, j))
            char = board[i][j]
            subtrie = trie.get_subtrie(char)            
            
            if subtrie:
                if subtrie.has_word:
                    output.add(subtrie.word)  
                dfs(i + 1, j, subtrie)
                dfs(i, j + 1, subtrie)
                dfs(i - 1, j, subtrie)
                dfs(i, j - 1, subtrie)
            board_visited.remove((i, j))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, prefixTree)

        return list(output)
    

board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
board_certain = [["b", "a", "c", "k"]]
words = ["bat","cat","back","backend","stack"]

s = Solution()

print(s.findWords(board, words))
            