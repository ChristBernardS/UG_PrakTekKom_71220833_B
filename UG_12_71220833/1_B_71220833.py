print('SELAMAT DATANG DI PROGRAM PEMBUATAN PIRAMIDA BERLUBANG')
angka = int(input('Masukan Angka : '))
for i in range(0, angka-1, 1):
    print((' '*(angka-i))+('*'*(i-(i-1)))+' ')
    for j in range(2, angka+1):
        print('*', end=' ')
    print('')
print((' '+'*'*(angka))+('*'*(angka-1)))
