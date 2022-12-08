print('SELAMAT DATANG DI PROGRAM PEMBUATAN PIRAMIDA BERLUBANG')
angka = int(input('Masukan Angka : '))
for i in range(0, angka-1, 1):
    print((' '*(angka-i))+('*'*(i-(i-1))), end='')
    for j in range(1):
        print('*', end=' ')
    print('')
print((' '+'*'*(angka))+('*'*(angka-1)))
