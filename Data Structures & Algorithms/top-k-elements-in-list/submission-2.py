class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = set(nums)
        hashmap_numbers: dict[int, int] = {}

        for number in numbers:
            hashmap_numbers[number] = nums.count(number)
        hashmap_sorted: dict[int, int] = dict(sorted(hashmap_numbers.items(), key=lambda item: item[1], reverse=True)[:k])
        return [num for num in hashmap_sorted.keys()]
