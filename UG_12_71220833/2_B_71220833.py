print('~~~ Selamat Datang di Kalkulator Sederhana ~~~')
a = input('Masukkan operator matematika yang ingin Anda hitung: ')
while True:
    if a == '+':
        angka1 = int(input('Mau penjumlahan berapa: '))
        angka2 = int(input('Print berapa banyak: '))
        for i in range(angka2):
            print(f'{i+1} + {angka2-i} = {(i+1)+(angka2-i)}')
    elif a == '-':
        angka1 = int(input('Mau pengurangan berapa: '))
        angka2 = int(input('Print berapa banyak: '))
        for i in range(angka2):
            print(f'{i+1} + {angka2-i} = {(i+1)-(angka2-i)}')
    elif a in ('x', 'X'):
        angka1 = int(input('Mau perkalian berapa: '))
        angka2 = int(input('Print berapa banyak: '))
        for i in range(angka2):
            print(f'{i+1} X {angka2-i} = {(i+1)*(angka2-i)}')
    elif a == ':':
        angka1 = int(input('Mau pembagian berapa: '))
        angka2 = int(input('Print berapa banyak: '))
        for i in range(angka2):
            print(f'{i+1} : {angka2-i} = {(i+1)/(angka2-i)}')
    else:
        print('Maaf, Operator Matematika yang Anda cari  belum tersedia.')
        break
    pernyataan = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ')
    if pernyataan in ('T', 't'):
        print('Terima Kasih dan Sampai Jumpa Lagi!')
        break
    elif pernyataan in ('Y', 'y'):
        continue
    else:
        print('ERROR\nPilih Y atau T\nUlangi Program')
        break
