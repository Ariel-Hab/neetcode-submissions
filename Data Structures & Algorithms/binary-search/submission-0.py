class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums) -1 
        while lower <= higher:
            index = (lower + higher)//2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                lower = index + 1
            else:
                higher = index - 1
            
        return -1