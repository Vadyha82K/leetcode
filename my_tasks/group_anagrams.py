# 49 Group anagrams (LeetCode)
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            counts = [0] * 26  #Так как в английском алфавите 26 букв, а в задании указано, что буквы только строчные
            for char in word:
                