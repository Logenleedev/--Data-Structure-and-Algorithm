# 口诀
1. 加元素
2. 数 valid
3. while valid 
4. 算长度/other operation
5. discard

```python 
from collections import defaultdict
start = 0
valid = 0
pointer = 0

need, window = defaultdict(int), defaultdict(int)

# update count if necessary

for i in range(len(s)):
    element = s[i]

    window[s[i]] += 1

    if element in need.keys():
        if window[element] == need[element]:
            valid += 1
    
    while valid == len(need.keys()):
        (any necessary operation)


        discard = s[pointer]
        
        if discard in need.keys():
            if window[discard] == need[discard]:
                valid -= 1

            window[discard] -= 1
            if window[discard] == 0:
                del window[discard]

        pointer += 1

```
   