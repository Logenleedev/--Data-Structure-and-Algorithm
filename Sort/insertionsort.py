# Time complexity O(n^2)
def insertionSort(seq):

    index = range(1, len(seq))
    for i in index:
        value = seq[i]

        while i > 0 and (seq[i] < seq[i - 1]):
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1
    return seq

a = [3,2,1,4,5,10,6]
print(insertionSort(a))