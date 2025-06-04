# 🧠 NeetCode Blind 75 - Problem 26: Remove Duplicates from Sorted Array
# ✅ Remove duplicates in-place from sorted array, return new length.
#
# Approach:
#   - Use two pointers: one for writing next unique (i), one for scanning (j).
#   - Only write a value if it's different from previous unique.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  (in-place, no extra arrays)
# ---------------------------------------------------------

def removeDuplicates(nums):
    """
    Removes duplicates from sorted array in-place and returns the new length.
    """
    if not nums:
        return 0

    i = 1  # Pointer for the next unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1

    return i

# ---------------------------------------------------------
# 🔍 Dry Run Example:
# Input: [0,0,1,1,1,2,2,3,3,4]
#
# Start: i=1, j=1
# nums[j]=0 == nums[i-1]=0 (skip)
# nums[j]=1 != nums[i-1]=0 (write at nums[1]=1, i=2)
# nums[j]=2 != nums[i-1]=1 (write at nums[2]=2, i=3)
# nums[j]=3 != nums[i-1]=2 (write at nums[3]=3, i=4)
# nums[j]=4 != nums[i-1]=3 (write at nums[4]=4, i=5)
# End array: [0,1,2,3,4,...]
# Return: 5
# ---------------------------------------------------------
#
# Complexity:
# - Time: O(n)  One pass through nums
# - Space: O(1) No extra arrays
# ---------------------------------------------------------
