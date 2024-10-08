# Define the TrieNode class
class TrieNode:
    def __init__(self):
        # Each node will have a dictionary of children (to store the next characters)
        self.children = {}  
        # This flag marks whether the current node is the end of a word
        self.endOfWord = False  

# Define the WordDictionary class
class WordDictionary:
    
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()

    # Method to add a word to the Trie
    def addWord(self, word: str) -> None:
        # Start at the root node
        cur = self.root
        
        # Traverse each character in the word
        for c in word:
            # If the character is not already a child of the current node, create a new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node (corresponding to the character)
            cur = cur.children[c]
        
        # Once all characters are added, mark the last node as the end of the word
        cur.endOfWord = True

    # Method to search for a word in the Trie
    # This method supports searching with '.' as a wildcard (which can match any character)
    def search(self, word: str) -> bool:
        
        # Depth-First Search (DFS) helper function to recursively search through the Trie
        def dfs(j, root):
            # Start at the current node (root in the first call)
            cur = root

            # Loop through the characters in the word starting from index j
            for i in range(j, len(word)):
                c = word[i]

                # If the current character is a '.', it acts as a wildcard
                # We need to explore all possible children at this point
                if c == ".":
                    # Loop through all children nodes of the current node
                    for child in cur.children.values():
                        # Recursively search the rest of the word starting from the next character (i + 1)
                        if dfs(i + 1, child):
                            return True  # If any path returns True, the search is successful
                    # If no paths return True, return False (no match found for the wildcard)
                    return False
                else:
                    # If the current character is not in the children, return False (no match)
                    if c not in cur.children:
                        return False
                    # Move to the next node (corresponding to the current character)
                    cur = cur.children[c]
            
            # After the loop, check if we are at a node that is the end of a word
            return cur.endOfWord

        # Start the DFS from the root node, beginning at index 0 of the word
        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)