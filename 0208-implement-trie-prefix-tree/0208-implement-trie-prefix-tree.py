    
    #Create TRieNode class first with children and a flag to signal when we are at the end of a word
    #We need a current so we know where we are
    # each time we insert a word we want to change isword into a True
    #Each time we look for a word in search we want to return isword
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]              
        return cur.isWord
        
        
                
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for p in prefix:
            if p not in cur.children:
                return False
            
            cur = cur.children[p]
                
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)