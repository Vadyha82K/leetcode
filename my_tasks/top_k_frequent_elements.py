# 347 Top K Frequent Elements
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            res[count].append(num)

        final_res = []

        for i in range(len(res) - 1, 0, -1):
            for num in res[i]:
                final_res.append(num)
                if len(final_res) == k:
                    return final_res


sol = Solution()

print(sol.topKFrequent([1,1,1,2,2,3], 2))
