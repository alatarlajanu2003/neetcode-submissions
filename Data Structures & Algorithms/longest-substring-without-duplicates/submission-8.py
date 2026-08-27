# abcad
# abcb

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        longest = 0
        seen = set()

        while left < len(s):
            seen.add(s[left])

            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1

            longest = max(longest, right - left)

            if right >= len(s):
                break
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

                right = max(right, left + 1)

        return longest


            