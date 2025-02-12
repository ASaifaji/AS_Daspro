# Garis Versi 1

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# Titik Koordinat
# make_point(a,b): 2 int --> point
# make_point(a,b): membuat titik dari dua buah nilai x,y
# REALISASI
def make_point(a,b):
    return [a,b]

# Garis
# make_garis(P1,P2): 2 point --> garis
# make_garis(P1,P2) membuat garis dengan penyusun dua buah titik
# REALISASI
def make_garis(P1,P2):
    return [P1,P2]




# DEFINISI DAN SPESIFIKASI SELEKTOR

# Absis
# absis(P): point --> int
# absis(P): mengembalikan nilai x dari sebuah titik
# REALISASI
def absis(P):
    return P[0]

# Ordinat
# ordinat(P): point --> int
# ordinat(P): mengembalikan nilai y dari sebuah titik
# REALISASI
def ordinat(P):
    return P[1]

# Titik awal
# titik_awal(G): garis --> point
# titik_awal(G) mengembalikan titik awal dari sebuah garis
# REALISASI
def titik_awal(G):
    return G[0]

# Titik akhir
# titik_akhir(G): garis --> point
# titik_akhir(G) mengembalikan titik akhir dari sebuah garis
# REALISASI
def titik_akhir(G):
    return G[1]

# Gradien
# gradien(G): garis --> 2 point --> float
# gradiean(G): mencari gradien dari suatu garis
# REALISASI
def grad(G):
    return ( ( ordinat(titik_akhir(G)) - ordinat(titik_awal(G)) ) / ( absis(titik_akhir(G)) - absis(titik_awal(G)) ) )

# DEFINISI DAN SPESIFIKASI PREDIKAT TERHADAP GARIS
# is_sejajar: 2 garis --> boolean
# is_sejajar(G1,G2) benar jika garis 1 dan garis 2 sejajar
# REALISASI
def is_sejajar(G1,G2):
    if grad(G1) == grad(G2):
        return True
    else:
        return False

# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP GARIS
# titik_potong_x: garis --> point
# titik_potong_x(G) memberikan titik potong garis yang diperpanjang terhadap sumbu x
# REALISASI
def titik_potong_x(G):
    return [round(-(ordinat(titik_awal(G))-(grad(G)*absis(titik_awal(G))))/grad(G),5) , 0]

# Aplikasi
import sys
exec(''.join(sys.stdin.readlines()))