from collections import Counter
class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False