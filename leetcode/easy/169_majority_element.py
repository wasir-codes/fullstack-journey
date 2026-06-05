# LeetCode #169 - Majority Element
# Approach: HashMap - count occurrences, return element exceeding n/2
# Time: O(n) | Space: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > len(nums) / 2:
                return num