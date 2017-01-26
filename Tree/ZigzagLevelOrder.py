class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level = 1
        currentLevelNum = 1
        nextLevelNum = 0
        resultList = []
        levelList = []
        while queue:
            node = queue.popleft()
            levelList.append(node.val)
            currentLevelNum -= 1
            if node.left:
                queue.append(node.left)
                nextLevelNum += 1
            if node.right:
                queue.append(node.right)
                nextLevelNum += 1
            if currentLevelNum == 0:
                if level % 2 == 1:
                    resultList.append(levelList)
                else:
                    levelList.reverse()
                    resultList.append(levelList)
                levelList = []
                currentLevelNum = nextLevelNum
                nextLevelNum = 0
                level += 1
        return resultList