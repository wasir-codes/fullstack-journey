# LeetCode #268 - Missing Number
# Approach: Math formula — expected sum minus actual sum
# Time: O(n) | Space: O(1)

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum