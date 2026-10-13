# left:  (, [, {
# right: ), ], }

# [{, [, (]
# ) => pop from queue => ( check if they are complementary
# ( => add to queue

# so on until queue is empty

# if right found and queue empty => return false

class Solution:

    def isValid(self, s: str) -> bool:

        open_to_close = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in open_to_close:
                stack.append(c)
            else:
                if not stack or c != open_to_close[stack.pop()]:
                    return False
                else:
                    continue

        return not stack




