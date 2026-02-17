"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.stack = []
        if not root:
            return None
        
        def build(root):
            if not root:
                return
            if root.left:
                self.stack.append(root.left)
            if root.right:
                self.stack.append(root.right)
        
        def link(list1):
            rp = None
            for i in list1[::-1]:
                i.next = rp
                rp = i
        
        self.stack1 = [root]
        while self.stack1:
            for i in self.stack1:
                build(i)
            link(self.stack)
            self.stack1 = self.stack
            self.stack = []
        return root