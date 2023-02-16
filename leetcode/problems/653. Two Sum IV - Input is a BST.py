class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, k, seen):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left, k, seen) or dfs(node.right, k, seen)
        
        seen = set()
        return dfs(root, k, seen)