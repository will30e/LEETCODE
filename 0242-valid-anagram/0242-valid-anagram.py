class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount_s, charCount_t = {}, {}

        for char in s:
            charCount_s[char] = 1 + charCount_s.get(char,0)

        for chars in t:
            charCount_t[chars] = 1 + charCount_t.get(chars,0)

        if charCount_s == charCount_t:
            return True

        else:
            return False