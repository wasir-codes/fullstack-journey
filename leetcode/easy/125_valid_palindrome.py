# LeetCode #125 - Valid Palindrome
# Approach: Clean string, compare with reverse
# Time: O(n) | Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [char.lower() for char in s if char.isalnum()]
        return cleaned == cleaned[::-1]