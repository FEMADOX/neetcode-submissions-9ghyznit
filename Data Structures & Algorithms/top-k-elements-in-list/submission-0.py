class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = set(nums)
        hashmap_numbers: dict[str, int] = {}
        # numbers_count: list[int] = []

        for number in numbers:
            # if not nums.count(number) >= k:
            #     continue
            hashmap_numbers[str(number)] = nums.count(number)
            # numbers_count.append(number)
        hashmap_sorted: dict[str, int] = dict(sorted(hashmap_numbers.items(), key=lambda item: item[1], reverse=True)[:k])
        return [int(num) for num in hashmap_sorted.keys()]
