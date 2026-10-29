import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search range for speed k: from 1 up to the largest pile
        left, right = 1, max(piles)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total hours needed to eat all piles at speed 'mid'
            total_hours = sum((p + mid - 1) // mid for p in piles)
            
            if total_hours <= h:
                # Speed is feasible; record it and try to find a smaller valid speed
                ans = mid
                right = mid - 1
            else:
                # Too slow; increase eating speed
                left = mid + 1
                
        return ans