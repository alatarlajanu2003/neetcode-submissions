# 1 2 + => [1, 2] => + (not a num) => 1 + 2, [] => [3]
# 1 2 + 3 * 4 - => 1 => [1] => 2 => [1, 2] => + => [3] => 3 => [3, 3] => * => [9] => 4 => - => [5] => return 5

import operator

class Solution:

    def division_truncated_to_zero(self, a: int, b: int):
        return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': self.division_truncated_to_zero
        }

        for token in tokens:
            if token.isdigit() or token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                result = operations[token](second, first)
                stack.append(result)

        return stack.pop()