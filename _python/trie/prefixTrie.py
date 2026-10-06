class PrefixTree:

    def __init__(self):
        self.has_word = False
        self.children = {}    

    def insert(self, word: str, index = 0) -> None:
        if (index == len(word)):
            self.has_word = True
            return

        char = word[index]
        if (char not in self.children):
            self.children[char] = PrefixTree()
        self.children[char].insert(word, index + 1)
        

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
        




prefixTree.insert("dog")
print(prefixTree.search("dog"))
print(prefixTree.startsWith("dog"))
print(prefixTree.search("do"))
print(prefixTree.startsWith("do"))
print(prefixTree.startsWith("dogs"))