# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if (not root):
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def maxDepth(self, root: TreeNode | None) -> int:
    #     if not root:
    #         return 0
    #     depth = 1
    #     children = deque()
    #     if root.left:
    #         children.append(root.left)
    #     if root.right:
    #         children.append(root.right)

    #     while children:
    #         depth += 1
    #         for num in range(len(children)):
    #             child = children.popleft()
    #             if child.left:
    #                 children.append(child.left)
    #             if child.right:
    #                 children.append(child.right)
    #     return depth