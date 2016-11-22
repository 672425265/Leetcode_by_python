# coding: utf-8
'''
Given a root node reference of a BST and a key,
delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).
Example:
root = [5,3,6,2,4,null,7]
key = 3
    5
   / \
  3   6
 / \   \
2   4   7
Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
    5
   / \
  4   6
 /     \
2       7
Another valid answer is [5,2,6,null,4,null,7].
    5
   / \
  2   6
   \   \
    4   7
'''

'''
首先根据BST（二叉查找树）的性质，找到目标节点cur及其父节点pre
如果cur不存在，则直接返回root
记ncur为取代cur位置的节点，默认令ncur = cur.right
如果cur拥有左孩子，则将其右孩子链接到左孩子的最大子节点的右侧，令cur = cur.left
然后修正pre与ncur之间的关系
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        pre, cur = None, root
        while cur and cur.val != key:
            pre = cur
            if key < cur.val:
                cur = cur.left
            elif key > cur.val:
                cur = cur.right
        if not cur:
            return root
        ncur = cur.right
        if cur.left:
            ncur = cur.left
            self.maxChild(cur.left).right = cur.right
        if not pre:
            return ncur
        if pre.left == cur:
            pre.left = ncur
        else:
            pre.right = ncur
        return root

    def maxChild(self, root):
        while root.right:
            root = root.right
        return root

'''
Java Solution:
public class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null){
            return null;
        }
        if(key < root.val){
            root.left = deleteNode(root.left, key);
        }else if(key > root.val){
            root.right = deleteNode(root.right, key);
        }else{
            if(root.left == null){
                return root.right;
            }else if(root.right == null){
                return root.left;
            }
            root.val = findMax(root.left).val;
            root.left = deleteNode(root.left, root.val);
        }
        return root;
    }

    private TreeNode findMax(TreeNode node){
        while(node.right != null){
            node = node.right;
        }
        return node;
    }
}
'''