#Soal 2
#Cek beasiswa

def cek_beasiswa(semester, status, nilai1, nilai2, nilai3, nilai4, nilai5):

    def nilai_angka(nilai):
        if nilai == 'A':
            return 4
        elif nilai == 'B':
            return 3
        elif nilai == 'C':
            return 2
        elif nilai == 'D':
            return 1
        elif nilai == 'E':
            return 0
        
    if status.lower() == 'aktif' or status.lower() == 'tidak cuti' and 3 <= semester <= 8:
        rata_rata = (nilai_angka(nilai1) + nilai_angka(nilai2) + nilai_angka(nilai3) + nilai_angka(nilai4) + nilai_angka(nilai5)) / 5
        if rata_rata >= 3.3:
            if nilai_angka(nilai1) >= 3 and nilai_angka(nilai2) >= 3 and nilai_angka(nilai3) >= 3 and nilai_angka(nilai4) >= 3 and nilai_angka(nilai5) >= 3:
                return 'berhak'
    return 'tidak berhak'


hasil_beasiswa = cek_beasiswa(5, 'aktif', 'A', 'B', 'B', 'B', 'A')
print(hasil_beasiswa)  # Output: 'berhak'

hasil_beasiswa = cek_beasiswa(2, 'engga ada kabar', 'A', 'C', 'B', 'D', 'E')
print(hasil_beasiswa)  # Output: 'tidak berhak'