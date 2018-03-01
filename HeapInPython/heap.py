import heapq

class Heap(object):
    def __init__(self):
        self._heap = []
        
    def push(self, val):
        heapq.heappush(self._heap, val)
    
    def pop(self):
        item = heapq.heappop(self._heap)
        return item
        
    def empty(self):
        return self.size() == 0

    def top(self):
        if self.empty():
            raise IndexError
        else:
            return self._heap[0]

    def size(self):
        return len(self._heap)
    
    def __iter__(self):
        return self
    
    def next(self):
        if len(self._heap):
            return self.pop()
        else:
            raise StopIteration
            
    def heapify(self):
        heapq.heapify(self._heap)


class MaxHeap(Heap):
    def __init__(self, vals=[]):
        super(MaxHeap,self).__init__()
        self._heap[:] = [-val for val in vals ]
        self.heapify()
        
    def push(self, val):
        super(MaxHeap,self).push(-val)
    
    def top(self):
        return -super(MaxHeap,self).top()

    def pop(self):
        return -super(MaxHeap,self).pop()

class MinHeap(Heap):
    def __init__(self, vals=[]):
        super(MinHeap,self).__init__()
        self._heap[:] = [val for val in vals ]
        self.heapify()
        