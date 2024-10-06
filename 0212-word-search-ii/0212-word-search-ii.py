# Define a node in the Trie
class TrieNode:
    def __init__(self):
        # Dictionary to hold child nodes for each character
        self.children = {}
        # Boolean flag to indicate if this node is the end of a word
        self.isWord = False
        
    # Method to add a word to the Trie
    def addWord(self, word):
        cur = self
        # Traverse each character in the word
        for c in word:
            # If character is not a child of current node, create a new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node corresponding to the character
            cur = cur.children[c]
        # Mark the current node as the end of a word
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a Trie and add all words to it
        root = TrieNode()
        for w in words:
            root.addWord(w)  # Corrected to match the method name defined in TrieNode
        
        # Get dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        # Use a set to store the results to avoid duplicates
        res, visit = set(), set()
        
        # Depth-first search (DFS) helper function for searching words on the board
        def dfs(r, c, node, word):
            # If the current position is out of bounds, already visited, or character not in Trie, return
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r, c) in visit):
                return
            
            # Mark the cell as visited
            visit.add((r, c))
            # Move to the next node in the Trie for the current character
            node = node.children[board[r][c]]
            # Append the character to the current word
            word += board[r][c]
            
            # If the current node marks the end of a word, add it to the results
            if node.isWord:
                res.add(word)
            
            # Explore all 4 directions: down, up, right, left
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            # Unmark the cell as visited (backtrack)
            visit.remove((r, c))
        
        # Start DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        # Return the list of found words
        return list(res)
