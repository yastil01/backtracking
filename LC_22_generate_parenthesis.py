class Solution:
    def helper(self, res, curr, n_left, n_right):
        if n_left==0 and n_right==0:
            res.append(curr)
        
        if n_left < 0 or n_right < 0:
            return
        
        self.helper(res, curr+'(', n_left-1, n_right)
        if n_right > n_left: 
            self.helper(res, curr+')', n_left, n_right-1)
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        res = []
        self.helper(res, '', n, n)
        return res
