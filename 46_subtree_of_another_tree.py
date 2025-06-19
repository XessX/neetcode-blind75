# 🌳 NeetCode Blind 75 - Problem 46: Subtree of Another Tree
# ✅ Return True if subRoot is a subtree of root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(s, t):
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

def isSubtree(root, subRoot):
    """
    Checks if subRoot is a subtree of root.
    Args:
        root (TreeNode): The root of the main tree.
        subRoot (TreeNode): The root of the subtree to check.
    Returns:
        bool: True if subRoot is a subtree of root, False otherwise.
    """
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# Optional: Example usage / Test
# if __name__ == "__main__":
#     # Example trees for manual test
#     pass
