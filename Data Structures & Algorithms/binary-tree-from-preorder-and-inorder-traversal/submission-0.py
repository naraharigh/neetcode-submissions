# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find index of root in inorder to split left and right subtrees
        mid = inorder.index(root_val)
        
        # Left subtree inorder: inorder[:mid], preorder: preorder[1:mid+1]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Right subtree inorder: inorder[mid+1:], preorder: preorder[mid+1:]
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
