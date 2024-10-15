#first build a TrieNode with children and a flag indicating when when we are at the end of the word
# to add a word into the list put current at the root node and iterate through the words in the root nodes children
# after set the flag to True after adding the word
#for search run dfs on it if the 

class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
                
            cur = cur.children[w]
            
        cur.word = True
        

    def search(self, word: str) -> bool:
        
        
        def dfs(j,root):
            cur = root

            for w in range(j,len(word)):
                c = word[w]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(w + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0,self.root)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)