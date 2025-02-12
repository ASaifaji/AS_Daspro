# keterangan angka

def ket_angka(n):
    if 0<=n<10:
        return "satuan"
    elif 10<=n<100:
        return "puluhan"
    elif 100<=n<1000:
        return "ratusan"
    elif 1000<=n<10000:
        return "ribuan"
    elif 10000<=n<100000:
        return "puluhribuan"

N = int(input())
print(ket_angka(N))