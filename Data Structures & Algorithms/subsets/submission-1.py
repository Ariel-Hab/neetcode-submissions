from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i:int)->None: # The idea is the following: To make a decision tree. What if this number is in this subset and what if it is not
            #first i check if i already finished the array
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # what if the subset has this number
            subset.append(nums[i])
            dfs(i+1)

            #what if it doesnt
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

            
