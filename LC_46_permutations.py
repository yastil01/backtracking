class Solution:
    def helper(self, curr, nums, res):
        if not nums:
            res.append(curr)
            return
        
        for i in range(len(nums)):
            self.helper(curr+[nums[i]], nums[:i]+nums[i+1:], res)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        self.helper([], nums, res)
        return res
