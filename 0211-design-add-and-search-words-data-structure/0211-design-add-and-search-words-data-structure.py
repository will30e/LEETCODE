class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        
        def dfs(j,root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for c in cur.children.values():
                        if dfs(i + 1, c):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
                        
        return dfs(0,self.root)
                        
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)