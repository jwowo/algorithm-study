class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def sumTotal(node):
            if not node: return 0
            if not node.left and not node.right: return node.val
            
            left_sum = sumTotal(node.left)
            right_sum = sumTotal(node.right)
            self.ans += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val
        
        sumTotal(root)
        return self.ans