# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sum):
            if not node:
                return False
            if node:
                sum = sum + node.val

            if not node.left and not node.right:
                return targetSum == sum

            if node.left or node.right:
                
                return  dfs(node.left,sum) or dfs(node.right,sum)
            
                        
            if sum == targetSum:
                return True    
            return False

        sum = 0 
        return dfs(root,sum)

        