#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
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
        if not head or not head.next:
            return head
        frist = head
        second = head
        # while second:
        #     if frist and frist.val > second.val:
        #         second.next = frist
        #         second = second.next
        #     elif not frist:
        #         second.next = frist
        #         second = second.next
        #         break
        #     frist = frist.next
        # 代码简化
        while frist:
            if frist.val > second.val:
                second = second.next
            else:
                second.next = frist.next
            frist = frist.next
        return head

# @lc code=end

