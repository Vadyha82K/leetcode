from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, num in enumerate(nums):
            number = target - num

            if number in numbers:
                return [numbers[number], i]
            
            numbers[num] = i