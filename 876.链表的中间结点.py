#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        # 快慢指针，快指针走两步，慢指针走一步
        # 假设慢指针走了3步，那么快指针走了3*2步
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
# @lc code=end
