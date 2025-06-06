# 🧠 NeetCode Blind 75 - Problem 33: Combination Sum
# ✅ Find all unique combinations of candidates that sum to target.
#
# Approach:
#   - Use backtracking/DFS.
#   - At each step, try using current candidate (can use again), or skip to next.
#
# Time Complexity: O(N^target/min), N=#candidates (roughly exponential)
# Space Complexity: O(target/min) (recursion depth and output)
# --------------------------------------------------------------

def combinationSum(candidates, target):
    """
    Returns all unique combinations of candidates that sum to target.
    Each candidate may be used unlimited times.
    """
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # use again
            path.pop()  # backtrack

    backtrack(0, [], 0)
    return res

# --------------------------------------------------------------
# 🔍 Dry Run Example:
# candidates = [2,3,6,7], target=7
# Try 2: [2]→[2,2]→[2,2,2]→[2,2,2,2] (too much), backtrack
# Try 2,2,3: [2,2,3]=7, add to result
# Try 3: [3], [3,3], [3,3,3] (too much), backtrack
# Try 7: [7]=7, add to result
# Output: [[2,2,3],[7]]
# --------------------------------------------------------------
#
# Complexity:
# - Time: O(N^target/min)
# - Space: Output + recursion stack
# --------------------------------------------------------------
