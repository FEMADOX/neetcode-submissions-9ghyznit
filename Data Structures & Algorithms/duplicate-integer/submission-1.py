class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        before_numbers = [nums[0]]
        for number in nums[1:]:
            if  number in before_numbers:
                return True
            before_numbers.append(number)
        return False