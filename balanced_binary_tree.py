from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        verdict = True

        def dfs(self, node: Optional[TreeNode], depth: int):
            nonlocal verdict
            if not node:
                return depth
            left_depth = dfs(self, node.left, depth + 1)
            right_depth = dfs(self, node.right, depth + 1)

            if abs(left_depth - right_depth) > 1: verdict = False
            return max(left_depth, right_depth)

        dfs(self, root, 0)
        return verdict
