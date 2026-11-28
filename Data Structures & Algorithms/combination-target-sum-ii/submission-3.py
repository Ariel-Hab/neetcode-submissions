from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i: int, total: int) -> None:
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Decision 1: Include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # Decision 2: Exclude candidates[i] AND all its duplicates
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res