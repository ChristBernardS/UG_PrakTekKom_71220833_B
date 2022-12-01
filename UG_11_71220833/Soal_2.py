def funPalindrome(kata):
    return kata == kata[::-1]


inputkata = str(input('Masukan Kata: '))
palindromekata = funPalindrome(inputkata)

if palindromekata:
    print(f'Yes\nJika Dibalik: {inputkata}')
else:
    print(f'No\nJika Dibalik: {inputkata}')
