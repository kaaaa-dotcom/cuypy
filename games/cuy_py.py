import random
import cuy
# from libry2 import continue_game
# from libry2 import end_game

list_Num = [1,2,3,4]

def start():
  while True:
     Bentuk_Jalan = "|*|"
     Jalan_Buntu = [Bentuk_Jalan]*4

     position = random.randint(1,4)

     Jalan = Jalan_Buntu.copy() # tempat posisi jalan
     Jalan[position - 1] = "|:|"

     Jalan_Buntu = "   ".join(Jalan_Buntu)
     Jalan = "   ".join(Jalan)


     print(f"coba perhatikan Jalan disamping ini\n\n{Jalan_Buntu}")

     pilihan_user = int(input(f"\nMenurut-mu MANA jalan yang bisa di lalui [1/2/3/4] = ")) # JADI PR

     if pilihan_user in list_Num:
      print(f"Pilihan-mu adalah {pilihan_user}")
      if pilihan_user == position:
        print("\n","\t",Jalan )
        print(f"\nSelamat 🏆lo Menang.., ternyata jalan yang bisa dilalui berada di No.{position}")
      else:
        print("\n","\t",Jalan )
        print(f"\nSalah.., 🤬🤬 WAH GOBLOK LU JALAN NYA TUH DI NO.{position}")
     else:
        print('Yang bener ajaaa..!')

    
     play_again = input(f"Main Terus Gaa [y/n] = ")
     if play_again == 'n':
        cuy.options()
        break
     elif play_again == 'y':
        print('\nLanjuuuttt...!')
    

if __name__ == '__main__':
    start()

