from collections import deque
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        sorted_nums = sorted(nums)
        self.heap = deque(sorted_nums[-k:])

    def add(self, val: int) -> int:
        temp = deque()
        inserted = False
        
        while self.heap and len(temp) < self.k:
            largest_heap_number = self.heap.pop()
            if not inserted and val > largest_heap_number:
                temp.appendleft(val)
                inserted = True
            if len(temp) < self.k:
                temp.appendleft(largest_heap_number)
                
        # Handle the case where val wasn't inserted yet and we still need elements
        if not inserted and len(temp) < self.k:
            temp.appendleft(val)
            
        self.heap = temp
        return self.heap[0] # Since self.heap is sorted ascending and size k, index 0 is the kth largest
