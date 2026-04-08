class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq, key=lambda num: freq[num], reverse=True)
        return sorted_freq[:k]