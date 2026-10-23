# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1, arr2 = [], []

        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        arr1, arr2 = reversed(arr1), reversed(arr2)

        nr1 = int(''.join([str(digit) for digit in arr1]))
        nr2 = int(''.join([str(digit) for digit in arr2]))

        sum_nr = nr1 + nr2
        reversed_sum = reversed([int(digit) for digit in str(sum_nr)])

        result = ListNode()
        result_head = result
        for digit in reversed_sum:
            result.next = ListNode(digit)
            result = result.next

        return result_head.next

