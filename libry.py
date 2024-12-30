import socket
from time import sleep

PC_NAME = socket.gethostname()

def start_game():
    equal = "=" * (len(PC_NAME) + 6)
    print(equal)
    print(f"== {PC_NAME} ==")
    print(equal)

def Open_game(title):
    equal = "=" * (len(title) + 6)
    print(equal)
    print(f"== {title} ==")
    print(equal)

def Open_tools(title):
    equal = "=" * (len(title) + 6)
    print(equal)
    print(f"== {title} ==")
    print(equal)

def exit_program():
    print("sistem Akan Berhenti")
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Sistem Berhasil Dihentikan')
    exit()

def inform():
    sleep(1.5)
    print(" Hai... Welcome To ")
    sleep(2.5)
    print(" Py^Gme ")
    sleep(3.5)
    Open_game("Start To Py^Gme")

def inform2():
    sleep(1.5)
    print(" Hai... Welcome To ")
    sleep(2.5)
    print(" Py^ToOls ")
    sleep(3.5)
    Open_game("Start To Py^ToOls")

if __name__ == '__main__':
    start_game()
    exit()
    inform()
    inform2()

######################################

def mulai(title):
    equal = "=" * (len(title) + 6)
    print(equal)
    print(f'== {title} ==')
    print(equal)



