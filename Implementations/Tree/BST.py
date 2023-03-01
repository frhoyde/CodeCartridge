#!/usr/bin/env python3

class Node:
    """
      This is a Node
      """
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    """
      This is a BST Declaration
      """
    def __init__(self, root):
        self.root = None

    def inorder(self, root):
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)
