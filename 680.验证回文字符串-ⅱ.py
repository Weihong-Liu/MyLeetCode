#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]
    
    def str_remove(self, s , x):
        return s[:x] + s[x + 1:]

    def validPalindrome(self, s: str) -> bool:
        left,right = 0,len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.is_palindrome(self.str_remove(s,left)) or self.is_palindrome(self.str_remove(s,right))
        return True
# @lc code=end
