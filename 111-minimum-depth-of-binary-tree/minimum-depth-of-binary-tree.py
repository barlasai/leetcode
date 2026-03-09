# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS Approach 
        # time, space = O(n), O(h)
        if not root:
            return 0
        stack = [(root, 1)]
        min_depth = float("inf")
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return min_depth 

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS Approach 
        # time, space: O(n), O(h) where h = height of the tree 
        if not root:
            return 0

        if not root.left: 
            return 1 + self.minDepth(root.right)
        if not root.right: 
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS Approach 
        # time, space: O(n), O(w) where w = maximum width of the tree
        if not root:
            return 0 
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()

            if not node.left and not node.right:
                return depth 
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

        