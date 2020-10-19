class Solution:
    def helper(self, nums, target, curr, res):
        if target == 0:
            res.append(curr)
            return
        
        if not nums or target<0:
            return
        
        self.helper(nums, target-nums[0], curr+[nums[0]], res)
        self.helper(nums[1:], target, curr, res)
            
            
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        self.helper(nums, target, [], res)
        return res
