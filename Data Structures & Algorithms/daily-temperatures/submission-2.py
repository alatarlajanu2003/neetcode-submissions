# [30,38,30,36,35,40,28]
# 28 -> 28, [(28, 6)]
# 40 -> 40, [40]
# 35 -> 40, [40, 35]
# 36 -> 40, [40, 36]
# 30 -> 36, [40, 36, 30]
# 38 -> 40, [40, 38]
# 30 -> 38, [40, 38, 30]

# initiate the stack w the rightmost temp (temp, pos)
# as we go on, if the next temp is bigger than the top of the stack => remove elems until condition holds, calc distance w the top of the stack, insert the curr one. else if the curr temp < than the top => calc the dist and insert into the stack.

# next closest bigger nr

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[-1], len(temperatures) - 1)]
        result = [0]

        for i in range(len(temperatures) - 2, -1, -1):
            current_temp = temperatures[i]
            
            while stack and current_temp >= stack[-1][0]:
                stack.pop()
            
            if stack:
                result.append(stack[-1][1] - i)
            else:
                result.append(0)

            stack.append((current_temp, i))

        return result[::-1]
                