class Solution:

    def romanToInt(self, s: str) -> int:
        val = 0
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s)):
            # If the current numeral is smaller than the next one, subtract its value
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                val -= roman_map[s[i]]
            else:
                val += roman_map[s[i]]

        return val


            
        