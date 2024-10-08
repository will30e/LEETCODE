class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        lst = []
        i = 0
        while len(s) > i:
            if not s[i] in lst:
                lst.append(s[i])
                i += 1
                maxLength = max(maxLength,len(lst))
            else:
                lst.pop(0)
        return maxLength


