class Solution:
    def helper(self, curr, s, s_orig, res):
        if len(curr) == len(s_orig):
            res.append(curr)
            return
        
        for i in range(len(s)):
            if s[i].isalpha():
                self.helper(curr+(s[i].lower()), s[i+1:], s_orig, res)
                self.helper(curr+(s[i].upper()), s[i+1:], s_orig, res)
            else:
                curr = curr + s[i]
                
        if len(curr) == len(s_orig):
            res.append(curr)
        
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        self.helper('', s, s, res)
        return res
