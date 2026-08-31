class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}

        for num in range(len(nums)):
            complement = target-nums[num]
            if complement in nums_seen:
                return([nums_seen.get(complement), num])
            else:
                nums_seen[nums[num]] = num