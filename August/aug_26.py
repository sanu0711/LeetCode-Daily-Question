# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> list[int]:
        if root is None:
            return []
        stack=[root]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.children:
                stack.extend(node.children)
        return output[::-1]
    
result = Solution().postorder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2, []), Node(4, [])])) 

print(result) # [5, 6, 3, 2, 4, 1]