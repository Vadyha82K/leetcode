# 49 Group anagrams (LeetCode)
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            counts = [0] * 26  #Так как в английском алфавите 26 букв, а в задании указано, что буквы только строчные
            
            for char in word:
                counts[ord(char) - ord("a")] += 1

            counts = tuple(counts)
            if counts not in result:
                result[counts] = []
            result[counts].append(word)
        
        return list(result.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))