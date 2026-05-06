# LeetCode #217 - Contains Duplicate
# Approach: Set - add each number, return True if already seen
# Time: O(n) | Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False        
        