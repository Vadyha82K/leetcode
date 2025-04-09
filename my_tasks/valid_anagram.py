class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_s = {}
        counts_t = {}

        for count_s, count_t in zip(s, t):
            counts_s[count_s] = counts_s.get(count_s, 0) + 1
            counts_t[count_t] = counts_t.get(count_t, 0) + 1

        return counts_s == counts_t