# 🌳 NeetCode Blind 75 - Problem 51: Construct Binary Tree from Preorder and Inorder Traversal
# ✅ Build the binary tree from preorder and inorder traversal lists.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Reconstructs a binary tree from preorder and inorder traversal.
    Args:
        preorder (List[int]): Preorder traversal list.
        inorder (List[int]): Inorder traversal list.
    Returns:
        TreeNode: The root of the reconstructed tree.
    """
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    idx = inorder.index(root_val)

    # Recursively build left and right subtrees
    root.left = buildTree(preorder[1:1+idx], inorder[:idx])
    root.right = buildTree(preorder[1+idx:], inorder[idx+1:])

    return root

# Optional: Example usage / Test
# if __name__ == "__main__":
#     preorder = [3,9,20,15,7]
#     inorder = [9,3,15,20,7]
#     root = buildTree(preorder, inorder)
