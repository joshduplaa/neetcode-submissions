class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcounts = {}
        frequencies = [[] for i in range(len(nums)+1)]
        
        for item in nums:
            numcounts[item] = numcounts.get(item, 0) + 1
        
        for item, count in numcounts.items():
            frequencies[count].append(item)
        
        result = []
        for item in range(len(frequencies)-1, 0, -1):
            for letter in frequencies[item]:
                result.append(letter)
                if len(result)==k:
                    return(result)




