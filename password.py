import random
from colorama import Fore,Style
import cuy
from libry import start_game

def password():
  
  upper = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
  lawer = "abcdefghijklmnopqrstuvwxyz"
  numbers = "0123456789"

  all = upper + lawer + numbers
  length = 5
  password = "".join(random.sample(all, length))

  color = Fore.LIGHTMAGENTA_EX + password + Style.RESET_ALL

  print(f'Harap password yang kami berikan ({color}) Jangan sampai lupa')

  isi = input("\nMasukan Password yang sudah kami Berikan : ")
  if isi == password:
    print(" Verifikasi Berhasil ")
    start_game()
    cuy.options()
  else:
    print(" Verifikasi Gagal ")

if __name__ == '__main__':
  password()



