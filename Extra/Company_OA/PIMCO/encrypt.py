
def encryption(encrypted, k):
    temp = list(encrypted)
    
    dict = {}

    for i in range(26):
        dict[i] = chr(i + ord('a'))

    for i in range(len(temp)):
        ref = ord(temp[i].lower()) - ord('a') - k

        while ref < 0:
            ref += 26

        temp[i] = dict[ref].upper()

    return ''.join(temp)

print(encryption('VTAOG', 2))