#use a stack
# helper function to input the word inside
# reverse the stack and then check if it is the same as s

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def valid_p(c):
            return c.isalnum()            
        stack = []
            
        for char in s:
            if valid_p(char):
                stack.append(char.lower())


        reverse_stack = stack[::-1] 
        return stack == reverse_stack
                
        