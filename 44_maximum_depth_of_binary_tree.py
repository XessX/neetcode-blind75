# 🌳 NeetCode Blind 75 - Problem 44: Maximum Depth of Binary Tree
# ✅ Return the maximum depth (height) of a binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    Returns the maximum depth of a binary tree.
    Args:
        root (TreeNode): Root of the binary tree.
    Returns:
        int: Maximum depth (height) of the tree.
    """
    if not root:
        return 0
    # Recursively get max depth of left and right subtrees, add 1 for root
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# Optional: Example usage / Test
# if __name__ == "__main__":
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(maxDepth(root))  # Output: 3
