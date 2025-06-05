# 🧠 NeetCode Blind 75 - Problem 29: Search in Rotated Sorted Array
# ✅ Find the index of target in a rotated sorted array in O(log n) time.
#
# Approach:
#   - Use binary search.
#   - At each step, determine if the left half or right half is sorted.
#   - Decide which side to search based on target's value.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ---------------------------------------------------------------

def search(nums, target):
    """
    Returns the index of target if present in nums, else -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Target is in the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# ---------------------------------------------------------------
# 🔍 Dry Run Example:
# nums = [4,5,6,7,0,1,2], target = 0
# left=0, right=6, mid=3 (nums[3]=7)
#   Left half [4,5,6,7] is sorted, target not in [4,5,6,7], search right
# left=4, right=6, mid=5 (nums[5]=1)
#   Left half [0,1] is sorted, target in [0,1], search left
# left=4, right=4, mid=4 (nums[4]=0), target found!
# Returns 4
# ---------------------------------------------------------------
#
# Complexity:
# - Time: O(log n), binary search
# - Space: O(1), in-place
# ---------------------------------------------------------------
