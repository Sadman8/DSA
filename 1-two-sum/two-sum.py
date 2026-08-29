class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i, val in enumerate(nums):
            comp = target - val
            if comp in seen:
                return [seen[comp], i]
            seen[val] = i