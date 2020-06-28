class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        out = []
        map = { '2':'abc', 
                '3':'def', 
                '4':'ghi', 
                '5':'jkl', 
                '6':'mno', 
                '7':'pqrs', 
                '8':'tuv', 
                '9':'wxyz' }
        
        def helper(curr, index):
            if index >= len(digits):
                out.append(curr)
                return 
            
            for i in range(len(map[digits[index]])):
                curr += map[digits[index]][i]
                helper(curr, index+1)
                curr = curr[:-1]
            
        helper('', 0)
        return out
