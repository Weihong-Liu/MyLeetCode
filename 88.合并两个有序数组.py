#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 法一（不通用）：
        for n2 in nums2:
            nums1[m] = n2
            m += 1
        nums1 = nums1.sort()

        # 法二（通用）：
        i = m -1
        j = n -1
        cur = m + n -1
        while j >= 0 and i >= 0:
            if nums1[i] <= nums2[j]:
                nums1[cur] = nums2[j]
                j -= 1
            else:
                nums1[cur] = nums1[i]
                i -= 1
            cur -= 1
        if i < 0:
            for k in range(0,cur+1):
                nums1[k] = nums2[k]

# @lc code=end

