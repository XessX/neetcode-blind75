# Problem: Group Anagrams
# Given an array of strings, group the anagrams together.

from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word and use it as the key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    # Return grouped anagrams as a list of lists
    return list(anagram_map.values())


# Example usage
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
