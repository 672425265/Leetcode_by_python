class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = self.findIndex(inorder, root.val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:len(postorder)-1])
        return root

    def buildTree2(self, preorder, inorder):
        # write your code here
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = self.findIndex(inorder, root.val)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

    def findIndex(self, inorder, value):
        for i, val in enumerate(inorder):
            if val == value:
                return i