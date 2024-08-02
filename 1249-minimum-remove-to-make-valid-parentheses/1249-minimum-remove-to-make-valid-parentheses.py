class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        for w in s:
            if w == "(":
                res.append(w)
                count += 1
                
            elif w == ")" and count > 0:
                res.append(w)
                count -= 1
            
            elif w != ")":
                res.append(w)
                
        filtered = []
        
        for w in res[::-1]:
            if w == "(" and count > 0:
                count -= 1
            else:
                filtered.append(w)
        return "".join(filtered[::-1])
            
                
        