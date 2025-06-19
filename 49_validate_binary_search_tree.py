# 🌳 NeetCode Blind 75 - Problem 49: Validate Binary Search Tree
# ✅ Check if a binary tree is a valid BST (all left < node < all right, recursively).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    Determines if a binary tree is a valid BST.
    Args:
        root (TreeNode): The root of the tree.
    Returns:
        bool: True if tree is a valid BST, False otherwise.
    """
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        # Left: valid range is (low, node.val)
        # Right: valid range is (node.val, high)
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float('-inf'), float('inf'))

# Optional: Example usage / Test
# if __name__ == "__main__":
#     # root = TreeNode(2, TreeNode(1), TreeNode(3))
#     # print(isValidBST(root))  # Output: True
