# 🧠 NeetCode Blind 75 - Problem 16: Valid Palindrome
# ✅ Check if a string is a palindrome (ignoring non-alphanumeric and case)
#
# ----------------------------------------------------------
# For example: "A man, a plan, a canal: Panama"
# Is a palindrome after cleaning: "amanaplanacanalpanama"
#
# Approach: Two Pointers (left and right) move towards the center,
# skipping any non-alphanumeric characters, and comparing characters
# case-insensitively.
#
# Time Complexity: O(n)   (Each character is checked at most once)
# Space Complexity: O(1)  (No extra data structures used)
# ----------------------------------------------------------

def isPalindrome(s: str) -> bool:
    """
    Returns True if 's' is a palindrome, considering only alphanumeric characters and ignoring case.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # 🔁 Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # 🔁 Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1
        # 🔁 Compare characters (lowercase, so case doesn't matter)
        if s[left].lower() != s[right].lower():
            return False
        # Move both pointers toward the center
        left += 1
        right -= 1

    # If all characters matched, it's a palindrome
    return True

# ----------------------------------------------------------
# 🔍 Example Usage / Dry Run:
# s = "A man, a plan, a canal: Panama"
# Step 1: Ignore spaces, commas, colons
# Step 2: Lowercase all characters
# Step 3: Compare from both ends moving toward the center
# All characters match! Output: True
#
# print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(isPalindrome("race a car"))                      # Output: False
# ----------------------------------------------------------

# ----------------------------------------------------------
# Complexity Analysis:
# --------------------
# Time Complexity: O(n)
#   - Each character in the string is visited at most once
#   - Skipping non-alphanumerics only increases pointer movement, not total work
#
# Space Complexity: O(1)
#   - No extra arrays or data structures are created (we only use pointers)
#
# Why is this optimal?
# - We do not use extra memory to create a filtered string
# - We never revisit any character
# ----------------------------------------------------------
