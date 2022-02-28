#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
# @lc code=start
import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        gap = math.inf
        n = len(nums) - 1
        for i in range(len(nums)-2):
            now = nums[i]
            left = i+1
            right = n
            while left < right:
                sum = abs(target - (now+nums[left]+nums[right]))
                if sum < gap:
                    gap = sum
                    result = now+nums[left]+nums[right]
                if (now+nums[left]+nums[right]) > target:
                    right -= 1
                else:
                    left += 1 
        return result

# @lc code=end
s = Solution()
print(s.threeSumClosest([-26,-34,79,40,72,54,33,-15,49,-56,72,3,-11,-16,32,1,-28,65,55,36,49,-93,52,10,-70,-99,-36,37,85,-54,8,-7,-57,9,-44,-3,-1,6,69,55,-49,-13,21,-66,-70,-54,7,81,-34,42,-1,-36,-40,23,-91,-81,-63,-92,-9,21,8,-90,-37,-47,93,-14,33,63,-24,-49,-96,-20,89,75,0,-43,-72,-58,35,-45,-25,54,75,99,-69,79,-42,21,43,27,93,86,2,4,13,-98,74,-63,33,79,74,99,89,11,82,-76,42,70,-70,-47,89,87,61,8,43,62,77,-99,46,97,-15,-34,-99,0,44,83,24,94,-86,79,-55,-11,-67,-96,-87,-73,-30,24,-76,-96,-3,-51,-14,79,11,-60,64,29,14,42,-84,-68,87],-71))