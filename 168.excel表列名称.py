#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        number = columnNumber
        while number > 0:
            number -= 1
            i = number%26
            s += chr(ord('A')+i)
            number = number//26
        return s[::-1]
# @lc code=end



# s = "FXSHRXW"
# s = s[::-1]
# count = 0
# for i in range(len(s)):
#     char = ord(s[i])-ord('A') + 1
#     # print(ord(s[i])-ord('A'))
#     count += pow(26,i) * char
# print(count)

# s = ''
# number = 701
# while number > 0:
#     number -= 1
#     i = number%26
#     s += chr(ord('A')+i)
#     number = number//26
# s = s[::-1]
# print(s)
