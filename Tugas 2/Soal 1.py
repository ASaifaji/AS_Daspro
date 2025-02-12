#Soal 1
#Cari nilai tengah

def nilai_tengah(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    else:
        if a >= c:
            return a
        elif b <= c:
            return b
        else:
            return c

a = nilai_tengah(4,5,6)
print(a)


