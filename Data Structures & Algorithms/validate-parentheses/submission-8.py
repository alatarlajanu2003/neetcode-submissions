# left:  (, [, {
# right: ), ], }

# [{, [, (]
# ) => pop from queue => ( check if they are complementary
# ( => add to queue

# so on until queue is empty

# if right found and queue empty => return false

from collections import deque

class Solution:

    def isValid(self, s: str) -> bool:

        complement = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = deque()
        curr_index = 0

        while curr_index < len(s):

            if s[curr_index] in complement.keys():
                stack.append(s[curr_index])
                curr_index += 1

            else:
                if not stack or s[curr_index] != complement[stack.pop()]:
                    return False
                else:
                    curr_index += 1

        return not stack




