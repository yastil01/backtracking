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
    def helper(self, digits, res, curr):
        if not digits:
            res.append(curr)
            return
        
        for i in range(len(self.map[digits[0]])):
            self.helper(digits[1:], res, curr+self.map[digits[0]][i])
            
            
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        self.helper(digits, res, '')
        return res
