class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_only = [c.lower() for c in s if c.isalnum()]
        return alphanum_only == alphanum_only[::-1]