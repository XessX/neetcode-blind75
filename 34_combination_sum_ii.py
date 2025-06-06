# 🧠 NeetCode Blind 75 - Problem 34: Combination Sum II
# ✅ Find all unique combinations that sum to target, using each candidate once.
#   Duplicates in input, but results must be unique!
#
# Approach:
#   - Sort input to make duplicate skipping easy.
#   - Use backtracking/DFS: for each index, either include or skip.
#   - Skip duplicates at same tree depth.
#
# Time Complexity: O(2^n)
# Space Complexity: O(n) + output
# ------------------------------------------------------------

def combinationSum2(candidates, target):
    """
    Returns all unique combinations of candidates that sum to target.
    Each candidate can only be used once.
    """
    candidates.sort()
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            # Skip duplicates at same tree level
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res

# ------------------------------------------------------------
# 🔍 Dry Run Example:
# candidates = [1,1,2,5,6,7,10], target=8
# (After sorting)
# Try 1: [1]
#   Try 1: [1,1]...
#   Try 2: [1,2]...
#   Try 5: [1,5]...
#   etc...
# Skip 1 at i=1 if i>0 and same as previous
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
# ------------------------------------------------------------
#
# Complexity:
# - Time: O(2^n)
# - Space: O(n) + output
# ------------------------------------------------------------
