#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        answer = []
        # print(nums)
        for i in range(n-2):
            # print("i====",i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = n - 1
            while start < end:
                # print("start===",start,"----end===",end)
                # print("nums[i] + nums[start] + nums[end] = ",nums[i] + nums[start] + nums[end])
                if nums[i] + nums[start] + nums[end] == 0:
                    if start-1 > i and nums[start] == nums[start-1]:
                        start += 1
                        continue
                    answer.append([ nums[i], nums[start], nums[end]])
                    start += 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    end -= 1
        return answer

# @lc code=end

S = Solution()
print(S.threeSum([0,0,0,0]))