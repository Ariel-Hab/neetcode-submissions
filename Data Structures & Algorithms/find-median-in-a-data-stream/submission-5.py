class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap,num)
        else: 
            if num < self.max_heap[0]: 
                heapq.heappush(self.min_heap,-num) #asi al hacer pop me da el mas grande (el maximo de los mas chicos)      
                
            else:
                heapq.heappush(self.max_heap,num) 
            
            if len(self.max_heap) > len(self.min_heap)+1:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
            if len(self.min_heap) > len(self.max_heap)+1:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        
        
        # print(f"min: {self.min_heap}; max:{self.max_heap}")
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        else: 
            return (self.max_heap[0] - self.min_heap[0]) / 2
        