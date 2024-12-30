from libry import start_game, exit_program, inform
from games import cuy_py, madlibs
from tools import Calculate, Market

# this is ^^^^^^^ A.K.A module or library


def options(): # < this fucntion for meringkas a program
    
  user_choose = int(input('Menu Program:\n1.Games \n2.Tools \n3.Exit\n\nChoose :'))

# (user_choose) use for logic program

  if user_choose == 1:
    choose = input("A.cuypy\nB.madlibs\n\n[A or B] = ")
    if choose == 'A':
      inform()
      cuy_py.start()
    elif choose == 'B':
      inform()
      madlibs.start()
  elif user_choose == 2:
    choose = input("A.calculator\nB.Market\n\n[A or B] = ")
    if choose == 'A':
      Calculate.start()
    elif choose == 'B':
      Market.start()
  elif user_choose:
    exit_program()
  else:
    print('\npilih yang bener bego..!')

def main(): # < this funtion for, where from the program start
  start_game()
  options()

if __name__ == '__main__':
  main()

# ^^^^^^for view in terminal