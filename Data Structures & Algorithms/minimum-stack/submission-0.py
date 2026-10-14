# [], min_arr
# push -> append; [], 1 -> [1], 2 -> [1, 2]; maintain min_arr
# pop -> pop, [1, 2] -> [1]; error handeling; maintain min_arr
# top -> arr[-1]
# getMin -> 3, 4, 5, 2
#          [3, 3, 3, 2], if pop => then pop here as well

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_arr) == 0:
            self.min_arr.append(val)
        else:
            self.min_arr.append(min(self.min_arr[-1], val))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_arr.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        
