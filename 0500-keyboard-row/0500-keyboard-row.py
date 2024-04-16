class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        
        for word in words:
            newSet = set(word.lower())
            if newSet.issubset(first_row) or newSet.issubset(second_row) or newSet.issubset(third_row):
                ans.append(word)
                
        return ans
             