class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Helper function to check if a character is alphanumeric
        def is_alphanumeric(c):
            return c.isalnum()

        # Use a stack to store alphanumeric characters in lowercase
        stack = []

        # Build the stack with only alphanumeric characters in lowercase
        for char in s:
            if is_alphanumeric(char):
                stack.append(char.lower())

        # Create a reversed version of the stack
        reversed_stack = stack[::-1]

        # Compare original stack with the reversed one
        return stack == reversed_stack