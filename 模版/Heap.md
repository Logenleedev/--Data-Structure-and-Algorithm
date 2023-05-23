

维护k个最大元素

```python
for key, value in map.items():
    heapq.heappush(pri_que, (value, key))
        if len(pri_que) > k:
            heapq.heappop(pri_que)
```