#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        
        dic = {}
        def recur(root):
            
            if not root:
                return 0
            
            sum = recur(root.left) + recur(root.right) + root.val
            dic[sum] = dic.get(sum, 0) + 1
            
            return sum
        
        recur(root)
        
        dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        answer = [dic[0][0]]
        prev = dic[0][1]
        for i in range(1, len(dic)):
            number, count = dic[i]
            if count != prev:
                break
            answer.append(number)
        return answer
        
# @lc code=end

