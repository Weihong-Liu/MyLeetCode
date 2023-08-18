#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 法一（不通用）
        if len(set(nums)) == len(nums):
            return False
        return True
    
        # 法二（通用）
        count = dict.fromkeys(list(set(nums)), 0)
        for num in nums:
            count[num]+=1
            if count[num]>=2:
                return True
        return False
# @lc code=end

