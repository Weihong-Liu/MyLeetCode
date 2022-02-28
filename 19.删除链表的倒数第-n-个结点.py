#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
from typing import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 栈
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        head = ListNode(next = head)
        temp = head
        stack = []
        while temp:
            stack.append(temp)
            temp = temp.next
        # stack.reverse()
        # for i,node in enumerate(stack):
        #     if i == n - 1:
        #         stack[i+1].next = node.next
        #         break
        # 官方写法
        for i in range(n):
            stack.pop()
        temp = stack[-1]
        temp.next = temp.next.next
        return head.next
# @lc code=end

