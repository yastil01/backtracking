class Solution:
    def helper(self, nums, curr, res):
        if not nums:
            res.append(curr)
            return
        
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            self.helper(nums[:i]+nums[i+1:], curr+[nums[i]], res)
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
       
        nums.sort() 
        res = []
        self.helper(nums, [], res)
        return res
