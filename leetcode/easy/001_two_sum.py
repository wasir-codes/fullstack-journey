# LeetCode #1 - Two Sum
# Approach: HashMap - store complement and index, O(n) lookup
# Time: O(n) | Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i