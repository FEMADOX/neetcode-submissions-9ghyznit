class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = set(nums)
        hashmap_numbers: dict[str, int] = {}

        for number in numbers:
            hashmap_numbers[str(number)] = nums.count(number)
        hashmap_sorted: dict[str, int] = dict(sorted(hashmap_numbers.items(), key=lambda item: item[1], reverse=True)[:k])
        return [int(num) for num in hashmap_sorted.keys()]
