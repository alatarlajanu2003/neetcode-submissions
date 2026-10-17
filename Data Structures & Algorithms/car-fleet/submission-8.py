# 4, 1, 0, 7;  2, 2, 1, 1
# 0, 1, 4, 7 (ordered); 1, 2, 2, 1
# 1:  1, 3, 6, 8
# 2:  2, 5, 8, 9
# 3:  3, 7, 10, 10 (one fleet at step 3)
# 4:  4, 9, 10, 10
# 5:  5, 10, 10, 10 (second fleet at step 5)
#  third fleet will arrive at step 10

# 4: 10 - 4 / 2 = 3
# 1: 10 - 1 / 2 = 4.5 = 5
# 0: 10 - 0 / 1 = 10
# 7: 10 - 7 / 1 = 3

# 1, 6, 7; 1, 3, 1
# 2, 8, 8
# 3, 9, 9
# 4, 10, 10
# ...

# 6 = 10 - 6 / 3 ± 2 ! it was 3 because 10 - 7 / 1 = 3 (and since 7 is in front u say 3)

# rule is, u calculate for each in how long it arrives
# if in front steps > than in the back => back adjusts to the front

# 1 = 9
# 6 = 2
# 7 = 3

# 9, 2, 3


# 6 = 3

# Cars belong to the same fleet if they arrive at the destination at the same time.


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_steps = []
        for i in range(len(position)):
            pos_and_steps.append((position[i], (target - position[i]) / speed[i]))

        sorted_pos_and_steps = sorted(pos_and_steps)
        steps = [s for (p, s) in sorted_pos_and_steps]

        if steps != sorted(steps, reverse = True):
            for i in range(len(steps) - 2, -1, -1):
                if steps[i] < steps[i + 1]:
                    steps[i] = steps[i + 1]
        
        return len(set(steps))


        


        