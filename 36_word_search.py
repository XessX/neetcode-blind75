# 🧠 NeetCode Blind 75 - Problem 36: Word Search
# ✅ Search for a word in a 2D board, moving up/down/left/right, each cell once.
#
# Approach:
#   - Try every cell as starting point.
#   - Use DFS/backtracking to try building the word.
#   - Temporarily mark visited cells to avoid revisiting.
#
# Time Complexity: O(m*n*4^L), m*n board, L=word length
# Space Complexity: O(L), recursion stack
# ------------------------------------------------------------

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        tmp, board[r][c] = board[r][c], '#'
        found = (dfs(r+1, c, idx+1) or
                 dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or
                 dfs(r, c-1, idx+1))
        board[r][c] = tmp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

# ------------------------------------------------------------
# 🔍 Dry Run Example:
# See above board, word="ABCCED"
# Start from (0,0): A → right (B) → right (C) → down (C) → left (E) → up (D)
# If any path matches word, return True.
# ------------------------------------------------------------
#
# Complexity:
# - Time: O(m*n*4^L)
# - Space: O(L)
# ------------------------------------------------------------
