def gamewinner(string):


    w_count = 0
    b_count = 0
    
    for i in range(1, len(string) - 1):
        if string[i] == 'w' and string[i + 1] == 'w' and string[i - 1] == 'w':
            w_count += 1
        if string[i] == 'b' and string[i + 1] == 'b' and string[i - 1] == 'b':
            b_count += 1


    
    if w_count < b_count:
        return 'Bob'
    elif w_count > b_count:
        return 'Wendy'
    else:
        return 'Bob'
            

print(gamewinner("wwwwbbbbwww"))

