# 🌳 NeetCode Blind 75 - Problem 52: Binary Tree Maximum Path Sum
# ✅ Find the maximum path sum in a binary tree (path can start/end at any node).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    """
    Returns the maximum path sum of any path in the binary tree.
    Args:
        root (TreeNode): The root of the tree.
    Returns:
        int: The maximum path sum.
    """
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        # Only take positive gains; otherwise, use 0 (don't include negative paths)
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        # Path passing through this node (can be a "V" shape: left+node+right)
        local_max = node.val + left + right

        # Update global max_sum if this path is higher
        max_sum = max(max_sum, local_max)

        # Return max one-side gain to parent
        return node.val + max(left, right)

    dfs(root)
    return max_sum

# Optional: Example usage / Test
# if __name__ == "__main__":
#     # root = TreeNode(1, TreeNode(2), TreeNode(3))
#     # print(maxPathSum(root))  # Output: 6
