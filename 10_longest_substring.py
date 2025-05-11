# 🧠 NeetCode Blind 75 - Problem 10: Longest Substring Without Repeating Characters
# ✅ Goal: Find the length of the longest substring with no repeating characters
# ✅ Approach: Sliding Window with a Set (Two Pointers)

def lengthOfLongestSubstring(s):
    char_set = set()     # ✅ To track unique characters in current window
    left = 0             # ✅ Left pointer of sliding window
    max_length = 0       # ✅ Stores the max length found

    for right in range(len(s)):          # ✅ Move right pointer through each character
        while s[right] in char_set:      # 🔁 Found duplicate? Shrink window from left
            char_set.remove(s[left])     # Remove leftmost character
            left += 1                    # Move left pointer forward

        char_set.add(s[right])           # ✅ Add current (non-duplicate) character
        # ✅ Calculate current window size and update max
        max_length = max(max_length, right - left + 1)

    return max_length

# 🔍 Example usage:
# print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3

# ✅ Time Complexity: O(n) — each character added/removed once
# ✅ Space Complexity: O(k) — at most k unique characters in window
