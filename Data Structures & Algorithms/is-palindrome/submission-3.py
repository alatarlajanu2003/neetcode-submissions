# tababat
# tab bat
# tab  bat
# tabbat

class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        # version 2
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not self.alphaNum(s[start]):
                start += 1

            while start < end and not self.alphaNum(s[end]):
                end -= 1

            if start < end and s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True

        # # version 1
        # alphanum_only = [c.lower() for c in s if c.isalnum()]
        # return alphanum_only == alphanum_only[::-1]