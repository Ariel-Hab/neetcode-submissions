from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path: List[int], remaining: List[int]) -> None:
            if not remaining:
                res.append(path)
                return

            for i in range(len(remaining)):
                pick = remaining[i]
                rest = remaining[:i] + remaining[i + 1:]
                dfs(path + [pick], rest)

        dfs([], nums)
        return res