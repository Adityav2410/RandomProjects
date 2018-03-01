## A toy library in Python for MinHeap and MaxHeap




### Heap 
```
from heap import MinHeap, MaxHeap

vals = np.random.randint(25,size=10)
maxHeap = MaxHeap(vals)
minHeap = MinHeap(vals)
maxHeap.push(19)
minHeap.push(29)

print "MinHeap"
for x in minHeap:
    print x,
print "\n\n\nMaxHeap"
for x in maxHeap:
    print x,
```


#### Output
```
MinHeap
2 6 6 6 12 13 13 18 23 24 29 


MaxHeap
24 23 19 18 13 13 12 6 6 6 2

```