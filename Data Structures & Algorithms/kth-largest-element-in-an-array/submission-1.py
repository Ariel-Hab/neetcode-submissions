class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                a = heapq.heappop(heap)
        return heap[-k]