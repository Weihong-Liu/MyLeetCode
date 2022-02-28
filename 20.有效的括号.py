#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        else:
            Stack = []
            for ch in s:
                if ch == '(' or ch == '{' or ch == '[':
                    Stack.append(ch)
                elif ch == '}':
                    if len(Stack)!=0 and Stack[-1] == "{":
                        Stack.pop()
                    else:
                        return False
                elif ch == ']':
                    if len(Stack)!=0 and Stack[-1] == "[":
                        Stack.pop()
                    else:
                        return False
                elif ch == ')':
                    if len(Stack)!=0 and Stack[-1] == "(":
                        Stack.pop()
                    else:
                        return False
            if len(Stack)!=0:
                return False
            else:
                return True
# @lc code=end

