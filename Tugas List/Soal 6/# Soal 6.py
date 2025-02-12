# Soal 6

def MinList(S):
    patokan = 100000000000
    
    for sublist in S:
        if type(sublist) is list:
            for element in sublist:
                if element < patokan:
                    patokan = element
        else:
            if sublist < patokan:
                patokan = sublist

    return patokan

print(MinList([3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [2]]) )