# 🌳 NeetCode Blind 75 - Problem 47: Lowest Common Ancestor of a BST
# ✅ Given a BST root and two nodes, return their lowest common ancestor.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    """
    Finds the lowest common ancestor of nodes p and q in a BST.
    Args:
        root (TreeNode): Root of the BST.
        p (TreeNode): First node.
        q (TreeNode): Second node.
    Returns:
        TreeNode: The lowest common ancestor of p and q.
    """
    # BST property: left < root < right
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left  # Both in left subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right  # Both in right subtree
        else:
            return root  # Split here or match found
    return None

# Optional: Example usage / Test
# if __name__ == "__main__":
#     # Tree and node setup for testing
#     pass
