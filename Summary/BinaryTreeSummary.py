# coding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def getNodeSum(self, root):
        if root is None:
            return 0
        count = 1
        queue = []
        queue.append(root)
        while len(queue) > 0:
            cur = queue.pop()
            if cur.left is not None:
                queue.append(cur.left)
                count += 1
            if cur.right is not None:
                queue.append(cur.right)
                count += 1
        return count

    def getNodeSumRec(self, root):
        if root is None:
            return 0
        else:
            return self.getNodeSumRec(root.left) + self.getNodeSumRec(root.right) + 1

    def maxDepthRec(self, root):
        if root is None:
            return 0
        left = self.maxDepthRec(root.left)
        right = self.maxDepthRec(root.right)
        return max(left, right) + 1

    def maxDepth(self, root):
        if root is None:
            return 0
        depth = 0
        currentLevelNodes = 1
        nextLevelNodes = 0
        queue = []
        queue.append(root)
        while len(queue) > 0:
            cur = queue.pop()
            currentLevelNodes -= 1
            if cur.left is not None:
                queue.append(cur.left)
                nextLevelNodes += 1
            if cur.right is not None:
                queue.append(cur.right)
                nextLevelNodes += 1
            if currentLevelNodes == 0:
                depth += 1
                currentLevelNodes = nextLevelNodes
                nextLevelNodes = 0
        return depth

    def levelTraversal(self, root):
        if root is None:
            return
        queue = []
        res = []
        queue.append(root)

        while len(queue) > 0:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

        return res

    def getNodeNumKthLevelRec(self, root, k):
        if root is None or k < 1:
            return 0
        if k == 1:
            return 1
        numleft = self.getNodeNumKthLevelRec(root.left, k - 1)
        numright = self.getNodeNumKthLevelRec(root.right, k - 1)
        return numleft + numright

    def getNodeNumKthLevel(self, root, k):
        if root is None:
            return 0
        queue = []
        queue.append(root)

        i = 1
        currentLevelNodes = 1
        nextLevelNodes = 0

        while len(queue) > 0 and i < k:
            cur = queue.pop(0)
            currentLevelNodes -= 1
            if cur.left is not None:
                queue.append(cur.left)
                nextLevelNodes += 1
            if cur.right is not None:
                queue.append(cur.right)
                nextLevelNodes += 1

            if currentLevelNodes == 0:
                currentLevelNodes = nextLevelNodes
                nextLevelNodes = 0
                i += 1

        return currentLevelNodes

    def getNodeNumLeafRec(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.getNodeNumLeafRec(root.left) + self.getNodeNumLeafRec(root.right)

    def getNodeNumLeaf(self, root):
        if root is None:
            return 0

        queue = []
        queue.append(root)
        leafNodes = 0
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
            if cur.left and cur.right:
                leafNodes += 1

        return leafNodes

    def isSameTreeRec(self, p, q):
        if p is None or q is None:
            return p == q
        if p.val == q.val:
            return self.isSameTreeRec(p.left, q.left) and self.isSameTreeRec(p.right, q.right)
        else:
            return False

    def getNodePath(self, root, node, path):
        if root is None:
            return False
        path.append(root.val)

        if root == node:
            return True

        found = False
        found = self.getNodePath(root.left, node, path)

        if not found:
            found = self.getNodePath(root.right, node, path)

        if not found:
            path.pop()

        return found

    def lcs(self, root, n1, n2):
        if root is None:
            return None

        if root == n1 or root == n2:
            return root

        left = self.lcs(root.left, n1, n2)
        right = self.lcs(root.right, n1, n2)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left
        return right

    def binaryTreePaths(self, root):
        paths = []
        if root is None:
            return paths
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        for path in leftPaths:
            paths.append(str(root.val) + "->" + str(path))
        for path in rightPaths:
            paths.append(str(root.val) + "->" + str(path))

        if len(paths) == 0:
            paths.append(str(root.val))

        return paths

    def isCompleteBinaryTree(self, root):
        if root is None:
            return False

        queue = []
        queue.append(root)
        mustHaveNoChild = False
        result = True

        while len(queue) > 0:
            cur = queue.pop(0)
            if mustHaveNoChild:
                if cur.left is not None or cur.right is not None:
                    result = False
                    break
            else:
                if cur.left is not None and cur.right is not None:
                    queue.append(cur.left)
                    queue.append(cur.right)
                elif cur.left is not None and cur.right is None:
                    mustHaveNoChild = True
                    queue.append(cur.left)
                elif cur.left is None and cur.right is not None:
                    result = False
                    break
                else:
                    mustHaveNoChild = True

        return result

    def pathSum(self, root, sum):
        res = []
        path = []
        self.dfs(res, path, root, sum)
        return res

    def dfs(self, res, path, root, sum):
        if root is None:
            return
        sum -= root.val
        if root.left is None and root.right is None:
            if sum == 0:
                path.append(root.val)
                res.append([] + path)
                path.pop()
            return
        path.append(root.val)
        self.dfs(res, path, root.left, sum)
        self.dfs(res, path, root.right, sum)
        path.pop()


root = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(3)
n3 = TreeNode(2)
n4 = TreeNode(1)
n5 = TreeNode(6)
n6 = TreeNode(7)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

a = Solution()
# print a.getNodeSum(root)
# print a.maxDepthRec(root)
# print a.maxDepth(root)
# print a.levelTraversal(root)
common = a.lcs(root, n3, n4)
print common.val