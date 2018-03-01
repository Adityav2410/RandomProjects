## A toy library in Python for MinHeap and MaxHeap

```
vals = [2,4,9, 1, 4, 54,5]
heap = MaxHeap(vals)
heap.push(27)
heap.pop()
for x in heap:
    print x,

```
### Output
```
27 9 5 4 4 2 1
```

```
vals = [2,4,9, 1, 4, 54,5]
heap = MinHeap(vals)
heap.push(27)
heap.pop()
for x in heap:
    print x,

```
### Output
```
2 4 4 5 9 27 54
```