# tababat
# tab bat
# tab  bat
# tabbat

# Madam, in Eden, I'm Adam
#            _
#            _

# madamine d enimadam
# madaminedenimadam

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # version 2
        start = 0
        end = len(s) - start - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1

            while start < end and not s[end].isalnum():
                end -= 1

            if start < end and s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True

        # # version 1
        # alphanum_only = [c.lower() for c in s if c.isalnum()]
        # return alphanum_only == alphanum_only[::-1]