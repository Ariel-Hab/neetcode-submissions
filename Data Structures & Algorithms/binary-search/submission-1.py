import bisect
class Solution:    
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
    
        # Verificamos que no se salga de la lista y que coincida exactamente
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1