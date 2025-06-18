# 🌳 NeetCode Blind 75 - Problem 45: Same Tree
# ✅ Determine if two binary trees are identical (structure and values).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    """
    Checks if two binary trees are the same.
    Args:
        p (TreeNode): Root of the first tree.
        q (TreeNode): Root of the second tree.
    Returns:
        bool: True if trees are identical, False otherwise.
    """
    # Both are null, so they're the same
    if not p and not q:
        return True
    # One is null or values differ
    if not p or not q or p.val != q.val:
        return False
    # Recurse for left and right
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Optional: Example usage / Test
# if __name__ == "__main__":
#     t1 = TreeNode(1, TreeNode(2), TreeNode(3))
#     t2 = TreeNode(1, TreeNode(2), TreeNode(3))
#     print(isSameTree(t1, t2))  # Output: True
