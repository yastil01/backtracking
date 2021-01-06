# helper([1,1,2], []) 
#    helper([1,2], [1]) 
#        helper([2], [1, 1]) 
#            helper([], [1, 1, 2])
#                return
#            return
#        helper([1], [1, 2])
#            helper([], [1, 2, 1])
#                return
#            return
#    helper([1,2], [1]) 
class Solution:
    def helper(self, nums, temp):
        if not nums:
            self.res.append(temp)
            return 
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:], temp+[nums[i]])
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums:
            nums.sort()
        self.res = []
        self.helper(nums, [])
        return self.res
