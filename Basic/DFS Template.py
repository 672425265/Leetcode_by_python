# coding: utf-8

# Template 1: Traverse

def traverse(root):
    if root == None:
        return

    # do something with root
    traverse(root.left)
    # do something with root
    traverse(root.right)
    # do something with root

# Tempate 2: Divide & Conquer

def traversal(root):
    if root == None:
        return

    # Divide
    left = traverse(root.left)
    right = traversal(root.right)

    # Conquer
    result = merge from left and right
    return result