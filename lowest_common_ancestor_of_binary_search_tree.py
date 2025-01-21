class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root
        while True:
            if current_node.val > p.val and current_node.val > q.val:
                current_node = current_node.left
            elif current_node.val < p.val and current_node.val < q.val:
                current_node = current_node.right
            else:
                return current_node
