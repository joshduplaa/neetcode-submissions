class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {} #for finding the complement and its index

 #num dict to map indexes to values
        for i, num in enumerate(nums):
            complement = (target-num)
            if complement in nums and (i != nums.index(complement)):
                print(i, nums.index(complement))
                j = nums.index(complement)
                print([i, nums.index(complement)].sort(reverse=True))
                if(i>j):
                    [i, j] = [j, i]
                return([i,j])
            

            
            