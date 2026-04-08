class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(t) > len(s):
            return False

        word_1_letters = set(s)
        word_2_letters = set(t)

        if word_1_letters != word_2_letters:
            return False

        for word_1_letter in word_1_letters:
            if s.count(word_1_letter) != t.count(word_1_letter):
                return False
        return True
