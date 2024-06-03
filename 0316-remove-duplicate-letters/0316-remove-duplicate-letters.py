class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for idx, char in enumerate(s):
            last_occurrence[char] = idx
        result = []
        seen = set()
    
        i = 0
        while i < len(s):
            char = s[i]
            
            if char not in seen:
            # Maintain the result in increasing lexicographical order
            # Remove the last character in the result if it's greater than the current character
            # and it appears later in the string (so we can use it later)
                while result and char < result[-1] and i < last_occurrence[result[-1]]:
                    seen.remove(result.pop())
            
                # Add the current character to the result and mark it as seen
                result.append(char)
                seen.add(char)
        
            i += 1

        return ''.join(result)
        