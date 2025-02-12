# Mahasiswa Versi 1


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# Mahasiswa
# make_mhs: string, 2 integer --> mahasiswa
# make_mhs(nama,nilai_uts,nilai_uas) membentuk sebuah tipe bentukan mahasiswa yang berisikan nama, nilai UTS, dan nilai UAS.
# REALISASI
def make_mhs(nama,nilai_uts,nilai_uas):
    return [nama,nilai_uts,nilai_uas]

# DEFINISI DAN SPESIFIKASI PREDIKAT

# Cek Lulus
# is_lulus(M): mahasiswa --> boolean
# is_lulus(M) benar jika rata-rata nilai UTS dan nilai UAS lebih besar atau sama dengan 75.
# REALISASI
def is_lulus(M):
    return bool(75.0<=((M[1]+M[2])/2))

# DEFINISI DAN SPESIFIKASI OPERATOR
# Konversi Nilai
# konversi(M): mahasiswa --> character
# konversi(M) mengembalikan karakter hasil konversi nilai UAS mahasiswa.
# REALISASI
def konversi(M):
    if M[2]>=50:
        if M[2]>=60:
            if M[2]>=70:
                if M[2]>=80:
                    return "A"
                else:
                    return "B"
            else:
                return "C"
        else:
            return "D"
    else:
        return "E"

# APLIKASI
import sys
exec(''.join(sys.stdin.readlines()))