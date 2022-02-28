#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
from typing import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head = ListNode(next = head)
        curr = head
        while curr.next!=None and curr.next.next!=None:
            if curr.next.val != curr.next.next.val:
                curr = curr.next
            else:
                n = curr.next
                while n and curr.next.val == n.val:
                    n = n.next
                curr.next = n
        return head.next
# @lc code=end

