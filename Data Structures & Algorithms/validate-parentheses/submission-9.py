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

        for c in s:
            if c in complement:
                stack.append(c)
            else:
                if not stack or c != complement[stack.pop()]:
                    return False
                else:
                    continue

        return not stack




