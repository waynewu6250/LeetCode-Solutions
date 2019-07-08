class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans_list = []
        def backtrack(ans, opn, clse):
            if len(ans) == 2*n:
                ans_list.append(ans)
                return
            
            if opn < n:
                backtrack(ans+"(", opn+1, clse)
            if clse < opn:
                backtrack(ans+")", opn, clse+1)
        
        backtrack("", 0, 0)
        return ans_list