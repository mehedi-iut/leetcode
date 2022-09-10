class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child.keys():
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.child.keys():
                return False
            curr = curr.child[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.child.keys():
                return False
            curr = curr.child[char]
        return True