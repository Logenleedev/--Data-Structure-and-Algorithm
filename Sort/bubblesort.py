# Time complexity O(n^2)
def bubbleSort(seq):
    n = len(seq)

    for i in range(n - 1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j+1],seq[j] = seq[j],seq[j+1]
    return seq

a = [3,2,1,4,5,10,6]
print(bubbleSort(a))