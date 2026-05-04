# LeetCode #136 - Single Number
# Approach: XOR — duplicates cancel out, lonely number remains
# Time: O(n) | Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for i in nums:
            single_num = single_num ^ i
        return single_num