def validateIP(ip):
    
        
    array = ip.split(".")
    
    for segment in array:
        if segment.isnumeric() == False:
            return False 
        else:
            num = int(segment)
            if num < 0 or num > 255:
                return False 
        
    return True 
    
    
print(validateIP("0.0.0.300"))


# Time Complexity: O(n)
# Space Complexity: O(n)