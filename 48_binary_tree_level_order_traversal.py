# 🌳 NeetCode Blind 75 - Problem 48: Binary Tree Level Order Traversal
# ✅ Return level-by-level node values of a binary tree (BFS).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    Returns the level order traversal of a binary tree as a list of lists.
    Args:
        root (TreeNode): Root of the binary tree.
    Returns:
        List[List[int]]: Level order traversal.
    """
    res = []
    if not root:
        return res

    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res

# Optional: Example usage / Test
# if __name__ == "__main__":
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
