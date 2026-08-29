class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                
                # Count consecutive numbers upwards
                while (n + length) in num_set:
                    length += 1
                    
                # Update our maximum found so far
                if length > longest:
                    longest = length
                    
        return longest