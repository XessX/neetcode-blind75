# 🧠 NeetCode Blind 75 - Problem 31: Search in Rotated Sorted Array II
# ✅ Like regular rotated binary search, but handles duplicates.
#
# Approach:
#   - Use binary search.
#   - If nums[left] == nums[mid] == nums[right], move left++ and right--.
#   - Otherwise, proceed as in rotated binary search.
#
# Time Complexity: O(log n) average, O(n) worst (all duplicates)
# Space Complexity: O(1)
# ---------------------------------------------------------------

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        # If left, mid, and right are equal, can't determine side—skip duplicates
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        # Left half is sorted
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False

# ---------------------------------------------------------------
# 🔍 Dry Run Example:
# nums = [2,5,6,0,0,1,2], target=0
#
# 1. left=0, right=6, mid=3, nums[3]=0 → found, return True
#
# nums = [2,5,6,0,0,1,2], target=3
# Check left, mid, right, reduce search space, never found → return False
# ---------------------------------------------------------------
#
# Complexity:
# - Time: O(log n) on average, O(n) if many duplicates
# - Space: O(1)
# ---------------------------------------------------------------
