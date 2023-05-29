"""
Smallest Substring of All Characters (Minimum Window Substring)

Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str 
containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

"""

# five steps
# 1. count freq 
# 2. count valid 
# 3. while  valid based on condition 
# 4. discard 
# 5. decrease valid 

def get_shortest_unique_substring(arr, string):
    ref = [0] * 26 
    ans = [0] * 26 
    valid = 0
    length = float('inf')
    start = 0 
    res =  ''

    for i in range(len(arr)):
        ref[ord(arr[i]) - ord('a')] += 1


    for i in range(len(string)):
        # count freq 
        ans[ord(string[i]) - ord('a')] += 1 

        if ans[ord(string[i]) - ord('a')] == ref[ord(string[i]) - ord('a')]:
            valid += 1
        
            while valid == len(arr):
                # shrink the window
                if i - start + 1 < length:
                    length = i - start + 1
                    res = string[start : i + 1]

                discard = string[start]

                if ans[ord(discard) - ord('a')] == ref[ord(discard) - ord('a')]:
                    valid -= 1

                ans[ord(discard) - ord('a')] -= 1

                if ans[ord(discard) - ord('a')] < 0:
                    ans[ord(discard) - ord('a')] == 0
                
        

                start += 1
    return res

        
print(get_shortest_unique_substring(['x','y','z'], "xxxxxxyyyyyyz"))




