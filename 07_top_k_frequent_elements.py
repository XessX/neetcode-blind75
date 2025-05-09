# Problem: Top K Frequent Elements
# Return the k most frequent numbers from the input list.

def topKFrequent(nums, k):
    # Step 1: Count frequencies of each number
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # Step 2: Create buckets to store numbers by frequency
    freq = [[] for _ in range(len(nums) + 1)]
    for num, c in count.items():
        freq[c].append(num)

    # Step 3: Collect the top k frequent elements from high freq to low
    result = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            result.append(num)
            if len(result) == k:
                return result
