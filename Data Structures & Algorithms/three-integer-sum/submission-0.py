class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to easily use two pointers and skip duplicates
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate elements for the first position to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers for the remaining array
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # We need a larger sum, move left pointer right
                elif total > 0:
                    right -= 1 # We need a smaller sum, move right pointer left
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for the second position
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicate elements for the third position
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward to look for other combinations
                    left += 1
                    right -= 1
                    
        return res
        