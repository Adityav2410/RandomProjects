import heapq

class MaxHeap(object):
    
    def __init__(self):
        self._heap = []
    
    def __init__(self, vals):
        self._heap = []
        self._heap[:] = [-val for val in vals ]
        heapq.heapify(self._heap)
        
    def push(self, val):
        heapq.heappush(self._heap, -val)
    
    def pop(self):
        item = -heapq.heappop(self._heap)
        return item
        
    def size(self):
        return len(self._heap)
    
    def __iter__(self):
        return self
    
    def next(self):
        if len(self._heap):
            return self.pop()
        else:
            raise StopIteration
            
            
class MinHeap(object):
    def __init__(self):
        self._heap = []
    
    def __init__(self, vals):
        self._heap = []
        self._heap[:] = [val for val in vals ]
        heapq.heapify(self._heap)
        
    def push(self, val):
        heapq.heappush(self._heap, val)
    
    def pop(self):
        item = heapq.heappop(self._heap)
        return item
        
    def size(self):
        return len(self._heap)
    
    def __iter__(self):
        return self
    
    def next(self):
        if len(self._heap):
            return self.pop()
        else:
            raise StopIteration