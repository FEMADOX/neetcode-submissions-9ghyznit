class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for index in range(len(nums)):
            first_number = nums[index]
            second_number = target - first_number
            if second_number not in nums[index + 1:]:
                continue
            pairs.extend([index, nums.index(second_number, index + 1)])
            break
        return pairs