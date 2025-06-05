# 🧠 NeetCode Blind 75 - Problem 32: Subsets
# ✅ Return all possible subsets (the power set) of nums.
#
# Approach:
#   - Use backtracking/DFS: at each index, decide to include or not.
#
# Time Complexity: O(n * 2^n)  (n = len(nums), 2^n subsets)
# Space Complexity: O(n * 2^n) (for the output)
# ----------------------------------------------------------

def subsets(nums):
    """
    Returns all possible subsets (the power set) of nums.
    """
    res = []

    def backtrack(start, path):
        res.append(path[:])  # Add current subset to results
        for i in range(start, len(nums)):
            # Include nums[i] and recurse
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack

    backtrack(0, [])
    return res

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# nums = [1,2]
#
# backtrack(0, []): add []
#   - pick 1 → backtrack(1, [1]): add [1]
#       - pick 2 → backtrack(2, [1,2]): add [1,2]
#       - pop 2, backtrack ends
#   - pop 1
#   - pick 2 → backtrack(2, [2]): add [2]
#   - pop 2
# Output: [[], [1], [1,2], [2]]
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n * 2^n)
# - Space: O(n * 2^n)
# ----------------------------------------------------------
