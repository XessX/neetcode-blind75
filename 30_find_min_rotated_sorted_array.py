# 🧠 NeetCode Blind 75 - Problem 30: Find Minimum in Rotated Sorted Array
# ✅ Find the minimum element in a rotated sorted array in O(log n) time.
#
# Approach:
#   - Use binary search.
#   - At each step, if nums[mid] > nums[right], minimum is to the right.
#   - Otherwise, it's at mid or to the left.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ---------------------------------------------------------------

def findMin(nums):
    """
    Returns the minimum value in the rotated sorted array nums.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than the rightmost,
        # the minimum is in the right half.
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is at mid or in left half.
            right = mid

    # After loop, left == right and points to the minimum
    return nums[left]

# ---------------------------------------------------------------
# 🔍 Dry Run Example:
# nums = [4,5,6,7,0,1,2]
# left=0, right=6
# mid=3 (nums[3]=7) > nums[6]=2 --> left=4
# mid=5 (nums[5]=1) < nums[6]=2 --> right=5
# mid=4 (nums[4]=0) < nums[5]=1 --> right=4
# left == right == 4, nums[4]=0 is the minimum.
# ---------------------------------------------------------------
#
# Complexity:
# - Time: O(log n), binary search
# - Space: O(1)
# ---------------------------------------------------------------
