
## KMP

```python 3
def getnext(self, a, s):
    # length of the array
    # string 
    
    next = [0]*a
    j = 0
        
    next[0] = 0

        
    for i in range(1, len(s)):
        while j > 0 and s[j] != s[i]:
            j = next[j - 1]
            
        if s[j] == s[i]:
            j += 1
        next[i] = j
    return next 

```
