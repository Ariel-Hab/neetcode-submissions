class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subset=[]
        res=[]
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #pruebo con el elemento y sus duplicados
            subset.append(nums[i])
            
            dfs(i+1)

            #pruebo sin el elemento y los duplicados   
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            subset.pop()
            
            dfs(i+1)
        dfs(0)
        return res