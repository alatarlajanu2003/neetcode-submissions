# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4], n = 2
# iterate through the list, len -> 4
# which position to remove: 4 - 2 = 2
# iterate through the list again till i = 2, i starts from 0

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # length
        len_list = 0
        temp = head

        while temp:
            len_list += 1
            temp = temp.next

        # position to remove
        pos_to_remove = len_list - n

        # iterate till pos to remove
        temp = ListNode(next = head)
        head_temp = temp
        i = 0
        while i < pos_to_remove:
            temp = temp.next
            i += 1

        print(temp.val)

        temp.next = temp.next.next if temp.next else None

        return head_temp.next

        