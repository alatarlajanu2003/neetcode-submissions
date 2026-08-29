# abc

# l = -1

# lecaabee
#       r -> not in abc => reset {}, l = -1
#     l

# lecabee
#     r -> if len r - l + 1 == abc => true
#   l

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = -1
        original_character_freq = Counter(s1)
        window_character_freq = defaultdict(int)

        for right in range(len(s2)):
            if s2[right] not in original_character_freq:
                left = -1
                window_character_freq = defaultdict(int)
                continue

            if left < 0:
                left = right

            window_character_freq[s2[right]] += 1

            while window_character_freq[s2[right]] > original_character_freq[s2[right]]:
                window_character_freq[s2[left]] -= 1
                left += 1

            if right - left + 1 == len(s1):
                return True

        return False