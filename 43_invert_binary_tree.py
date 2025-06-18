# 🌳 NeetCode Blind 75 - Problem 43: Invert Binary Tree
# ✅ Given the root of a binary tree, invert the tree and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    """
    Inverts a binary tree recursively.
    Args:
        root (TreeNode): Root of the binary tree.
    Returns:
        TreeNode: Root of the inverted binary tree.
    """
    if not root:
        return None
    # Swap left and right
    root.left, root.right = root.right, root.left
    # Recur on children
    invertTree(root.left)
    invertTree(root.right)
    return root

# Optional: Example usage / Test
# if __name__ == "__main__":
#     root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
#     inverted = invertTree(root)
#     # Now root.left is 7, root.right is 2, etc.
