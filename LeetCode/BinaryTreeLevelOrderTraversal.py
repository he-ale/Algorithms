from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if(not root):
            return []
        
        ls= [[root.val]]
        aux: deque[TreeNode] = deque()

        if root.left:
            aux.append(root.left)
        if root.right:
            aux.append(root.right)

        while (aux):
            lsLevel= []
            for _ in range(len(aux)):
                node= aux.popleft()
                lsLevel.append(node.val)
                if (node.left):
                    aux.append(node.left)
                if (node.right):
                    aux.append(node.right)
            ls.append(lsLevel)
        return ls