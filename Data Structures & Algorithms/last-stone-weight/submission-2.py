import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate values to simulate a max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heavy1 = -heapq.heappop(max_heap)
            heavy2 = -heapq.heappop(max_heap)
            
            if heavy1 != heavy2:
                heapq.heappush(max_heap, -(heavy1 - heavy2))

        return -max_heap[0] if max_heap else 0