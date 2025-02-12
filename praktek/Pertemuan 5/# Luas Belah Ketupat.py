# Luas Belah Ketupat


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# Belah Ketupat
# make_belahketupat: 2 real --> belahketupat
# make_belahketupat(d1,d2) membentuk sebuah belahketupat dengan panjang diagonal 1 dan panjang diagonal 2.
# REALISASI
def make_belahketupat(d1,d2):
    return [d1,d2]


# DEFINISI DAN SPESIFIKASI OPERATOR

# Luas
# Luas(B): belahketupat --> real
# Luas(B) mengembalikan nilai luas dari belah ketupat B.
def Luas(B):
    return round(B[0]*B[1]/2,5)


# APLIKASI
import sys
exec(''.join(sys.stdin.readlines()))