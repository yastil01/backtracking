class Solution:
    def helper(self, curr, index, nums, res):
        if index == len(nums):
            res.append(curr)
            return res 
        
        self.helper(curr, index+1, nums, res)
        self.helper(curr + [nums[index]], index+1, nums, res)
        return res
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        
        res = []
        return self.helper([], 0, nums, res)
