from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int, total: int) -> None:
            
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return

            # Decision 1: Include nums[i] (stay at i so we can reuse it)
            subset.append(nums[i])
            dfs(i, total + nums[i])

            # Decision 2: Exclude nums[i] (move to i + 1)
            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res