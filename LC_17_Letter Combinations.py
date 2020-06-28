"""
Time Complexity = O(n^4)
Sapce Complexity = O(n)

a in abc
    curr = a
    helper(a, 1)
        d in def
            curr = ad
            helper(ad, 2): exit out
            curr = a
        e in def
            curr = ae
            helper(ae, 2): exit out
            curr = a
        f in def
            curr = af
            helper(af, 2): exit out
            curr = a
        curr = ''

b in abc
    ....
    ....
    ....
"""

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
