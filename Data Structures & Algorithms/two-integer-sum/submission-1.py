class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for num in range(0, len(nums)):
            compliment = target - nums[num]
            if compliment in seen:
                return [seen[compliment], num]
            seen[nums[num]] = num