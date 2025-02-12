# Volume balok


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# Balok
# make_balok: 3 real --> balok
# make_balok(p,l,t) membentuk sebuah balok dengan nilai panjang, lebar, dan tinggi.
# REALISASI
def make_balok(p,l,t):
    return [p,l,t]


# DEFINISI DAN SPESIFIKASI OPERATOR
# Volume
# volume(B): balok --> real
# volume(B) mengembalikan volume dari balok B.
# REALISASI
def volume(B):
    return round(B[0]*B[1]*B[2],5)

# APLIKASI
import sys
exec(''.join(sys.stdin.readlines()))