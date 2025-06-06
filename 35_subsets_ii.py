# 🧠 NeetCode Blind 75 - Problem 35: Subsets II
# ✅ Return all possible subsets, avoiding duplicates in output.
#
# Approach:
#   - Sort nums to cluster duplicates together.
#   - Use backtracking/DFS.
#   - At each recursion level, skip nums[i] if it’s a duplicate of nums[i-1].
#
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
# ----------------------------------------------------------

def subsetsWithDup(nums):
    nums.sort()
    res = []

    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            # Skip duplicates at same tree level
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res

# ----------------------------------------------------------
# 🔍 Dry Run Example:
# nums = [1,2,2]
# Sorted: [1,2,2]
# Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]
# ----------------------------------------------------------
#
# Complexity:
# - Time: O(n * 2^n)
# - Space: O(n * 2^n)
# ----------------------------------------------------------
