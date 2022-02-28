#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i=="#" and stack!=[]:
                stack.pop()
            elif i!="#":
                stack.append(i)
        s = "".join(stack)
        stack = []
        for i in t:
            if i=="#" and stack!=[]:
                stack.pop()
            elif i!="#":
                stack.append(i)
        t = "".join(stack)
        if s==t:
            return True
        else:
            return False
# @lc code=end

