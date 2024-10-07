class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root  # Start from the root node
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    # Find the shortest root for a given word
    def find_shortest_path(self, word):
        node = self.root
        prefix = ""

        for char in word:
            if char not in node.children:
                break

            node = node.children[char]
            prefix += char

            if node.isWord:
                return prefix

        return word  # Return the original word if no root is found

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Initialize the Trie
        trie = Trie()
        
        # Insert all roots into the Trie
        for dic in dictionary:
            trie.insert(dic)
            
        # Split the sentence into words
        words = sentence.split()
        
        result = []
        
        # Replace each word with its shortest root if found
        for word in words:
            root = trie.find_shortest_path(word)
            result.append(root if root else word)
        
        # Join the words with spaces to form the final sentence
        return " ".join(result)
