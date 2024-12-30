import cuy

def start():
    a = int(input('Masukan Angka :'))
    b = int(input('Masukan Angka :'))
    p = input("[+,-,*,/] = ")
    
    if p == '+':
        print(f'Hasilnya adalah {a + b}')
        u = input('y or n : ')
        if u == 'n':
            cuy.options()
        elif u == 'y':
            start()

    elif p == '-':
        print(f"Hasilnya adalah {a - b}")
        u = input('y or n : ')
        if u == 'n':
            cuy.options()
        elif u == 'y':
            start()

    elif p == '*':
        print(f'Hasilnya adalah {a * b}')
        u = input('y or n : ')
        if u == 'n':
            cuy.options()
        elif u == 'y':
            start()

    elif p == '/':
        print(f"Hasilnya adalah {a / b}")
        u = input('y or n : ')
        if u == 'n':
            cuy.options()
        elif u == 'y':
            start()

if __name__ == '__main__':
    start()