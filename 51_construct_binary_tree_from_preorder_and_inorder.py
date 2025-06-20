# 🌳 NeetCode Blind 75 - Problem 51: Construct Binary Tree from Preorder and Inorder Traversal
# ✅ Build the binary tree from preorder and inorder traversal lists.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # The value of the node (e.g., 3, 9, 20, ...)
        self.left = left        # The left child node
        self.right = right      # The right child node

def buildTree(preorder, inorder):
    # 1. Base Case: If either list is empty, there is no tree to build.
    if not preorder or not inorder:
        return None

    # 2. The first element in preorder is always the root of the (sub)tree.
    root_val = preorder[0]               # Take root value from first element
    root = TreeNode(root_val)            # Create a TreeNode for the root

    # 3. Find the root's index in inorder list.
    mid = inorder.index(root_val)        # This index splits left and right subtree

    # 4. Recursively build the left subtree
    #    preorder[1:1+mid]: the next 'mid' elements are left subtree nodes
    #    inorder[:mid]: everything left of root in inorder is left subtree
    root.left = buildTree(preorder[1:1+mid], inorder[:mid])

    # 5. Recursively build the right subtree
    #    preorder[1+mid:]: remaining elements are right subtree nodes
    #    inorder[mid+1:]: everything right of root in inorder is right subtree
    root.right = buildTree(preorder[1+mid:], inorder[mid+1:])

    # 6. Return the constructed node (which now has .left and .right set)
    return root


# Optional: Example usage / Test
# if __name__ == "__main__":
#     preorder = [3,9,20,15,7]
#     inorder = [9,3,15,20,7]
#     root = buildTree(preorder, inorder)
