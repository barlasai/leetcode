class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)