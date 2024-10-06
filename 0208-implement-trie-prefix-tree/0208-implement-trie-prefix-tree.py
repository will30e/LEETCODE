class TrieNode:
    def __init__(self):
        # Dictionary to hold child nodes for each character
        self.children = {}
        # Boolean flag to indicate the end of a word
        self.endOfword = False

# The main Trie (prefix tree) class
class Trie:

    def __init__(self):
        # The root of the Trie is an empty TrieNode
        self.root = TrieNode()

    # Method to insert a word into the Trie
    def insert(self, word: str) -> None:
        # Start from the root node
        cur = self.root
        
        # Traverse each character in the word
        for c in word:
            # If character is not a child of current node, create a new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node corresponding to the character
            cur = cur.children[c]
        # After inserting all characters, mark the end of the word
        cur.endOfword = True

    # Method to search for a complete word in the Trie
    def search(self, word: str) -> bool:
        # Start from the root node
        cur = self.root
        
        # Traverse each character in the word
        for c in word:
            # If character is not found, word does not exist in Trie
            if c not in cur.children:
                return False
            # Move to the next node
            cur = cur.children[c]
        # Return True if the current node marks the end of a word
        return cur.endOfword

    # Method to check if any word in the Trie starts with a given prefix
    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        cur = self.root
        
        # Traverse each character in the prefix
        for c in prefix:
            # If character is not found, prefix does not exist in Trie
            if c not in cur.children:
                return False
            # Move to the next node
            cur = cur.children[c]
        # If traversal completes without returning False, prefix exists
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)