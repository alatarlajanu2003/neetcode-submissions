"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # node creation
        head_pointer = head
        nodes = []

        while head_pointer:
            nodes.append(Node(x = head_pointer.val))
            head_pointer = head_pointer.next

        # nexts
        for i, node in enumerate(nodes):
            if i + 1 < len(nodes):
                node.next = nodes[i + 1]

        # for node in nodes:
        #     print(node.val, node.next.val if node.next else None)

        # randoms

        # 0: None
        # 1: 3
        # 2: 0
        # 3: 1

        # node of 3: (0, None)
        # node of 7: (1, None)
        # node of 4: (2, None)
        # node of 5: (3, None)

        # curr: is it's random non none and in the dict => no
        # curr: is it's random non none and in the dict? => yes (node of 5) => node of 7: (1, 3) ...

        head_pointer = head
        nodes_and_their_randoms_positions = {}
        i = 0

        while head_pointer:
            nodes_and_their_randoms_positions[head_pointer] = (i, None)
            i += 1
            head_pointer = head_pointer.next

        head_pointer = head
        while head_pointer:
            if head_pointer.random and head_pointer.random in nodes_and_their_randoms_positions:
                nodes_and_their_randoms_positions[head_pointer] = (nodes_and_their_randoms_positions[head_pointer][0], nodes_and_their_randoms_positions[head_pointer.random][0])
            head_pointer = head_pointer.next

        nodes_and_their_randoms_positions = {index: random_index for (index, random_index) in nodes_and_their_randoms_positions.values()}

        for i, node in enumerate(nodes):
            if not nodes_and_their_randoms_positions[i] is None:
                node.random = nodes[nodes_and_their_randoms_positions[i]]

        return nodes[0] if nodes else None

        