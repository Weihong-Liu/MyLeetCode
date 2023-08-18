#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
from typing import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pre1 = headA
        pre2 = headB
        stackA = []
        stackB = []
        lenA = 0
        lenB = 0
        while pre1:
            stackA.append(pre1)
            lenA += 1
            pre1 = pre1.next
        while pre2:
            stackB.append(pre2)
            lenB += 1
            pre2 = pre2.next
        node = None
        for i in range(min(lenA, lenB)):
            A = stackA.pop()
            B = stackB.pop()
            if A != B:
                break
            else:
                node = A 
        return node


# @lc code=end


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if( headA == None or headB == None ): 
            return None
        pointA = headA
        pointB = headB

        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointA