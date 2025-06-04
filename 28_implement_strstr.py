# 🧠 NeetCode Blind 75 - Problem 28: Implement strStr() / Find Substring
# ✅ Find the index of the first occurrence of needle in haystack.
#
# Approach:
#   - For each position in haystack, check if the substring matches needle.
#
# Time Complexity: O((N - L) * L), N = len(haystack), L = len(needle)
# Space Complexity: O(1) (ignoring output and input storage)
# ---------------------------------------------------------

def strStr(haystack, needle):
    """
    Returns the index of the first occurrence of needle in haystack, or -1 if not found.
    """
    L, N = len(needle), len(haystack)
    if L == 0:
        return 0  # Empty needle always matches at 0

    for i in range(N - L + 1):
        if haystack[i:i+L] == needle:
            return i

    return -1

# ---------------------------------------------------------
# 🔍 Dry Run Example:
# haystack = "sadbutsad", needle = "sad"
# i = 0: "sad" == "sad" --> return 0
#
# haystack = "leetcode", needle = "leeto"
# Try i = 0: "leetc" != "leeto"
# Try i = 1: "eetco" != "leeto"
# Try i = 2: "etcod" != "leeto"
# ... none match --> return -1
# ---------------------------------------------------------
#
# Complexity:
# - Time: O((N-L)*L), worst case check for every possible window
# - Space: O(1) (in-place checks, no extra arrays)
# ---------------------------------------------------------
