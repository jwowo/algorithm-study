# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS를 통해서 중위 순회하다가 
# low 보다 크거나 작은 수는 sum에 더하고 
# high 보다 크면 바로 return
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        
        def dfs(node):
            nonlocal answer
            if not node:
                return 
            
            dfs(node.left)
            if low <= node.val <= high:
                answer += node.val
            dfs(node.right)
            
        dfs(root)
        return answer