
## 判断质数

```python 
def isPrime(self, num):
        
    if num == 1:
        return False 
            
    for i in range(2, num):
        if  num % i == 0:
            return False 
                             
    return True 

# O(n) 不推荐
```


```python 
def isPrime(self, num):
        
    if num == 1:
        return False 
            
    for i in range(2, int(num ** 0.5) + 1):
        if  num % i == 0:
            return False 
                             
    return True 
# O(sqrt(n)) 优化版本
```

## XOR operation 
```python 
1 XOR 0 = 1
1 XOR 1 = 0 
0 XOR 1 = 1 
0 XOR 0 = 0 
```
