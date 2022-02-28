#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
from typing import *
from typing import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        pre = head
        length = 0
        while pre.next:
            length += 1
            pre = pre.next
        pre.next = head
        k = k % (length + 1)
        pre = head
        for i in range(length - k):
            pre = pre.next
        head = pre.next
        pre.next = None
        return head
# @lc code=end

