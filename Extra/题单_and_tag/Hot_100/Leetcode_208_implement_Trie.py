
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root 

        for c in word:
            # 两种情况
            # 1. 有
            # 2. 没有
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]

        cur.end = True 


    def search(self, word: str) -> bool:
        cur = self.root 

        for c in word:
            if c not in cur.children:
                return False 
            else:
                cur = cur.children[c]

        return cur.end 


    def startsWith(self, prefix: str) -> bool:
        cur = self.root 

        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]

        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Time Complexiy: O(n)
# Space Complexity: O(q): 

'''
q is the total length of all the word. Worse case:
every word is different. e.g. abc and def 
'''