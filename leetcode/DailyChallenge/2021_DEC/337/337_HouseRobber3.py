# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs를 이용한 풀이 방법
    def rob(self, root: Optional[TreeNode]) -> int:
         return max(self.dfs(root))
    
    def dfs(self, root: TreeNode):
        if not root:
            return (0, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))
    
    """
    # 처음 작성한 코드
    if root is None:
        return 0

    print(root)

    # dp = [[0] * 2 for _ in range()]
    rob_root = root.val
    dont_rob = self.rob(root.left) + self.rob(root.right)

    if root.left:
        rob_root += self.rob(root.left.left) + self.rob(root.left.right)
    if root.right:
        rob_root += self.rob(root.right.left) + self.rob(root.right.right)

    dp[root] = max(dont_rob, rob_root)
    return max(dont_rob, rob_root)
    """    
        
    """
    # cache를 이용한 방법
    @cache
    def rob(self, root: Optional[TreeNode]) -> int:
        # 비어있으면 0 반환
        if root is None:
            return 0
        
        rob_root = root.val
        dont_rob = self.rob(root.left) + self.rob(root.right)
        
        if root.left:
            rob_root += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob_root += self.rob(root.right.left) + self.rob(root.right.right)
        
        return max(dont_rob, rob_root)
    """