             


             
什么时候要想到用 heap?
关键字
1. k + adj (e.g. k smallest)
2. most + adj (e.g. most heavy blablabla)


维护k个最大元素

```python
for key, value in map.items():
    heapq.heappush(pri_que, (value, key))
        if len(pri_que) > k:
            heapq.heappop(pri_que)
```

几个常用的 API 
```python 
heapq.heapify()
heapq.heappush()
heapq.heappop()
```