#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
                i-=1
            i+=1
        return len(nums)
# @lc code=end

S = Solution()
S.removeElement([1,1,1,0,0],1)
