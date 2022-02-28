#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j)
                elif nums[j] > nums[i]:
                    break
            i += 1
        return len(nums)
        
# @lc code=end

S = Solution()
print(S.removeDuplicates([1,1,2]))
