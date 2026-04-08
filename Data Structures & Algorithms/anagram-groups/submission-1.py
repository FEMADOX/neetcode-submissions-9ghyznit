class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_anagrams_letters: dict[str, list[str]] = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in hashmap_anagrams_letters:
                hashmap_anagrams_letters[key] = [word]
                continue
            hashmap_anagrams_letters[key].append(word)
        return [anagrams_words for anagrams_words in hashmap_anagrams_letters.values()]