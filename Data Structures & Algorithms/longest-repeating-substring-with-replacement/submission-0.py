# AABABBA
# A => [1, 0, 0...], longest = 1
# A => [2, 0, 0...], longest = 2
# B => [2, 1, 0...], longest = 3
# A => [3, 1, 0...], longest = 4
# B => [3, 2, 0...], if window size - most freq elem > k => 5 - 3 = 2 > 1 => move left while not valid window:
# A -> [3 - 1, 2, 0...] => 4 - 2 > 1 => 
# A -> [2 - 1, 2, 0...] => 3 - 2 == 1
# update longest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_freq = [0] * 26
        longest = 0

        for right in range(len(s)):
            char_freq[ord(s[right]) - 65] += 1
            
            while (right - left + 1) - max(char_freq) > k:
               char_freq[ord(s[left]) - 65] -= 1
               left += 1

            longest = max(longest, right - left + 1)

        return longest