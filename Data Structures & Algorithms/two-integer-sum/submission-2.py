class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for index in range(len(nums)):
            second_number = target - nums[index]
            if second_number not in nums[index + 1:]:
                continue
            pairs.extend([index, nums.index(second_number, index + 1)])
            break
        return pairs