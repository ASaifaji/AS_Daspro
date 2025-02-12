# GAJI ZIRKA

def cek_gaji(n):
    if n==10000000:
        return "Gaji tetap"
    elif n>10000000:
        return "Dapat Bonus"
    else:
        return "Gaji dipotong"

gaji = int(input())
print(cek_gaji(gaji))