# ✅ NeetCode Blind 75 - Problem #08
# 🔸 Problem: Product of Array Except Self (Leetcode 238)
# ✅ Goal: Return an array such that each element at index i is the product of all the numbers in the input array except nums[i]
# 🔒 Constraint: Solve without using division and in O(n) time.

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # Step 1: Get length of input list
    n = len(nums)

    # Step 2: Initialize result array with all 1s
    res = [1] * n  # This will hold final results

    # Step 3: Compute prefix product for each index
    # prefix will store the product of all elements to the left of i
    prefix = 1
    for i in range(n):
        res[i] = prefix          # Set result[i] to current prefix
        prefix *= nums[i]       # Update prefix for next index
        # After loop: res[i] = product of elements left of i

    # Step 4: Compute postfix product for each index (right to left)
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix       # Multiply with product of elements right of i
        postfix *= nums[i]      # Update postfix for previous index

    return res

# 🔍 Example Usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = productExceptSelf(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected Output: [24, 12, 8, 6]

"""
🧠 Step-by-step Calculation for nums = [1, 2, 3, 4]

# After Prefix Pass:
res = [1, 1, 2, 6]    # Each index i = product of elements to the left of i

# After Postfix Pass:
res = [24, 12, 8, 6]  # Now each index i = left * right product (excluding self)

✅ Time Complexity: O(n)
✅ Space Complexity: O(1) extra space (ignoring the result array)
"""
