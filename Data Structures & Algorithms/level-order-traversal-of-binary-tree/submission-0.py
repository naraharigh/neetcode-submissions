# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        result= []
        while len(queue) > 0:
            print("level: ", level)
            re_1 = []
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                re_1.append(int(curr.val))
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(re_1)
            level += 1
        return result
        
        