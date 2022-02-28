#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = []
        for token in tokens:
            if token == "+":
                Stack.append(Stack.pop() + Stack.pop())
            elif token == "-":
                Stack.append(-Stack.pop() + Stack.pop())
            elif token == "*":
                Stack.append(Stack.pop() * Stack.pop())
            elif token == "/":
                Stack.append(int(1/Stack.pop() * Stack.pop()))
            else:
                Stack.append(int(token))
        return Stack.pop()
# @lc code=end

