# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 6, 1, 5, 2, 4, 3]
# [0, 3, 6, 4, 1, 2, 5]

# [0, 6, 1]
# [5, 2, 4, 3] -> 3, 4, 2, 5

#  5, 2, 4, 3
#  2, 5, 4, 3
#  2, 4, 5, 3
#  2, 4, 3, 5

#  2, 4, 3, 5 -> 4, 2, 3, 5 -> 4, 3, 2, 5

#  4, 3, 2, 5 -> 3, 4, 2, 5

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #  finding middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        curr = slow.next
        slow.next = None
        prev_node = None

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        # merge
        first, second = head, prev_node
        while second:
            tmp1, tmp2 = first.next, second.next
            second.next = tmp1
            first.next = second
            first, second = tmp1, tmp2

