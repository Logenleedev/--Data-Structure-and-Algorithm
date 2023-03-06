
## 数值计算
```python 
int(eval(f'{second_item} {item} {first_item}'))
```

## Sorted

```python 
num = sorted(num)
num = sorted(num, key = abs, reverse = True)
num.sort(key = lambda x: (-x[0], x[1]))
```

## Extend list

```python
num.extend([0] * count)
```

## Default dict
```python 3
from collections import defaultdict

a = defaultdict(list)
# => []

a = defaultdict(str)
# => ""

a = defaultdict(int)
# => 0
```

## Revserse list

```python 
ans[n:] = reversed(ans[n:])
```

## Stack and queue 

deque 

```python 
from collections import deque

# Initialize a queue 
q = deque()

# Add element 
q.append()
q.append()
q.append()

# Remove element from the left 
q.popleft()

# Remove element from the right 
q.pop() 
```


大顶堆/小顶堆：

堆是一种非线性结构，可以把堆看作一棵二叉树，也可以看作一个数组，即：堆就是利用完全二叉树的结构来维护的一维数组。

堆可以分为大顶堆和小顶堆。
大顶堆：每个结点的值都大于或等于其左右孩子结点的值。heap[k] >= heap[2*k+1] 和 heap[k] >= heap[2*k+2]
小顶堆：每个结点的值都小于或等于其左右孩子结点的值。heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]

如果是排序，求升序用大顶堆，求降序用小顶堆。

一般我们说 topK 问题，就可以用大顶堆或小顶堆来实现，
最大的 K 个：小顶堆
最小的 K 个：大顶堆

```python 

import heapq



li = [5, 7, 9, 1, 3]


heapq.heapify(li)

# heapq API
# https://docs.python.org/zh-cn/3/library/heapq.html


pri_que = []

for key, value in ref.items():
    heapq.heappush(pri_que, (value, key))

```



## Other 
Counter in python 

```python 
from collections import Counter 

a = [1, 2, 3, 3, 3, 4]

print(Counter(a)[1])
# 1

b = "mmmmmmmabbbsgstyxbg"

print(Counter(b)['m'])
# 7
```