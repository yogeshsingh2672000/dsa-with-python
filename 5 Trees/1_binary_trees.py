class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if root:
        print(root.val, end=" ")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.val, end=" ")
        inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.val, end=" ")

root = TreeNode(3)
root.left = TreeNode(26)
root.right = TreeNode(42)
root.left.left = TreeNode(54)
root.left.right = TreeNode(65)
root.right.left = TreeNode(12)
print("\nPreorder traversal of binary tree is")
preOrderTraversal(root)
print("\nInorder traversal of binary tree is")
inOrderTraversal(root)
print("\nPostorder traversal of binary tree is")
postOrderTraversal(root)
