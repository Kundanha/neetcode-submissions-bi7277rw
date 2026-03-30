class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord("a")
            if cur.children[index] == None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True
        
        