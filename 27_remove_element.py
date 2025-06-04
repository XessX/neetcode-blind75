# 🧠 NeetCode Blind 75 - Problem 27: Remove Element
# ✅ Remove all instances of val in-place and return new length.
#
# Approach:
#   - Use two pointers: one for writing (i), one for scanning (j).
#   - For each element not equal to val, write at nums[i], increment i.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# --------------------------------------------------------------

def removeElement(nums, val):
    """
    Removes all occurrences of val in-place from nums and returns the new length.
    """
    i = 0  # Pointer for next write position
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# --------------------------------------------------------------
# 🔍 Dry Run Example:
# Input: nums = [3,2,2,3], val = 3
#
# i=0, j=0: nums[0]=3 (skip)
# i=0, j=1: nums[1]=2 (write at nums[0]=2, i=1)
# i=1, j=2: nums[2]=2 (write at nums[1]=2, i=2)
# i=2, j=3: nums[3]=3 (skip)
#
# Output: 2, array is [2,2,...]
# --------------------------------------------------------------
#
# Complexity:
# - Time: O(n)    Each element is visited once
# - Space: O(1)   In-place, no extra space
# --------------------------------------------------------------
