def update_times(signal_one, signal_two):
    count = 0 
    
    max_signal = float('-inf')

    for i in range(len(signal_one)):
        if signal_one[i] == signal_two[i] and signal_one[i] > max_signal: 
            count += 1
            max_signal = max(max_signal, signal_one[i])
    
    return count 

signal_one = [1,2,3,3,3,5,4]
signal_two = [1,2,3,4,3,5,4]

print(update_times(signal_one, signal_two))

# Time Complexity: O(n)
# Space Complexity: O(1)