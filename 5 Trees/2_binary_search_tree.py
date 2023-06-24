# binary search tree (BST)
# tree which have strictly smaller value on left side
# and strictly greater value on right side of root
# (can't have duplicates) known as BST

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)

def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target) 
    elif target < root.val:
        return search(root.left, target)
    else:
        return True

print(search(root, 6))