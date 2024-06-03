class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                i += 1
            else:
                j += 1
                i += 1
            
        res = len(t) - j
        return res
            
        
        