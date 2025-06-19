# 🌳 NeetCode Blind 75 - Problem 50: Kth Smallest Element in a BST
# ✅ Return the k-th smallest value in a BST (in-order traversal).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    """
    Returns the k-th smallest value in a BST.
    Args:
        root (TreeNode): The root of the BST.
        k (int): 1-indexed k-th smallest.
    Returns:
        int: The k-th smallest node's value.
    """
    stack = []
    curr = root
    count = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right

# Optional: Example usage / Test
# if __name__ == "__main__":
#     # Example tree for manual test
#     pass
