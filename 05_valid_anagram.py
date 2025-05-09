# Problem: Valid Anagram
# Determine if two strings are anagrams of each other.

def isAnagram(s, t):
    # Step 1: If lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False

    # Step 2: Create a dictionary to count characters in s
    count = {}

    for char in s:
        # Add 1 to the character count if it exists, otherwise start from 0
        count[char] = 1 + count.get(char, 0)

    # Step 3: Subtract character counts using t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False  # More of this char in t than in s

    # Step 4: All counts balanced → it’s an anagram
    return True


# Example test cases
print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
