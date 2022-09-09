class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.max_word_len = 0
        
    def addWord(self, word):
        cur = self.root
        count = 0
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            count += 1
        self.max_word_len = max(count, self.max_word_len)
        cur.word = True
        
    def search(self, word):
        if len(word) > self.max_word_len:
            return False
        
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)