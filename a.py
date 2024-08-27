from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def traverse(root: TreeNode, level: int) -> str:
            if not root:
                return ''
            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)
        return str.rstrip(traverse(self, 0))


def build_tree(arr: list[int], i, n):
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2*i+1, n)
        root.right = build_tree(arr, 2*i+2, n)
    return root

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        temp = root
        sum = root.val
        while root is not None:
            if root.left is None and root.right is None:
                return sum == targetSum
            root = root.left
    def backtrackingSum(self, root, targetSum, sum):
        if self.isLeaf(root):
            if sum == targetSum:
                return targetSum

        if root.left:
            sum+=root.left.val
            self.backtrackingSum(root.left,targetSum, sum)
            sum-=root.left.val

        if root.right:
            sum+=root.right.val
            self.backtrackingSum(root.right,targetSum, sum)
            sum-=root.right.val
        
        return sum


    
    def isLeaf(self, node):
        return node.left is None and node.right is None
    

arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = build_tree(arr, 0, len(arr))
solver = Solution()
print(root.__repr__())
print(solver.backtrackingSum(root, 22, 5))