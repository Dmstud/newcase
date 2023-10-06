# игра крестики нолики
# формируем список, имитирующий поле игры
L = [["-"  for j in range(4)] for i in  range(4)]
L[0][0] = ''
L[0][1],L[1][0] = 1,1
L[0][2],L[2][0] = 2,2
L[0][3],L[3][0] = 3,3
# проверка на выигрыш
def victory(M) :
    if  M[1][1] == 'X' and M[1][2] == "X" and M[1][3] == 'X': return True
    elif M[2][1] == 'X' and M[2][2] == "X" and M[2][3] == 'X': return True
    elif M[3][1] == 'X' and M[3][2] == "X" and M[3][3] == 'X': return True
    elif M[1][1] == 'X' and M[2][1] == "X" and M[3][1] == 'X': return True
    elif M[1][2] == 'X' and M[2][2] == "X" and M[3][2] == 'X': return True
    elif M[1][3] == 'X' and M[2][3] == "X" and M[3][3] == 'X': return True
    elif M[1][1] == 'X' and M[2][2] == "X" and M[3][3] == 'X': return True
    elif M[1][3] == 'X' and M[2][2] == "X" and M[3][1] == 'X': return True
    elif M[1][1] == '0' and M[1][2] == "0" and M[1][3] == '0': return True
    elif M[2][1] == '0' and M[2][2] == "0" and M[2][3] == '0': return True
    elif M[3][1] == '0' and M[3][2] == "0" and M[3][3] == '0': return True
    elif M[1][1] == '0' and M[2][1] == "0" and M[3][1] == '0': return True
    elif M[1][2] == '0' and M[2][2] == "0" and M[3][2] == '0': return True
    elif M[1][3] == '0' and M[2][3] == "0" and M[3][3] == '0': return True
    elif M[1][1] == '0' and M[2][2] == "0" and M[3][3] == '0': return True
    elif M[1][3] == '0' and M[2][2] == "0" and M[3][1] == '0': return True
s = 1
# ход крестика, если mot - True, ход нолика,если mot - False
mot = True
# распечатываем поле для игры
for j in range(4): print(*L[j])
while s <= 9 :
     if mot == True:
              g = int(input('горизонтальная координата  крестика'))
              h = int(input ('вертикальная координата  крестика'))
# распечатываем поле с нанесенным Х
              L[g][h] = "X"
              for j in range(4): print(*L[j])
              s += 1
# изменяем mot , чтобы следущим циклом ввести нолик
              mot = False
# проверяем крестиков на выигрыш, в случае победы выходим из цикла
              if victory(L):
                  s = 11
                  print('победа крестиков')
     else:
          g = int(input('горизонтальная координата  нолика'))
          h = int(input ('вертикальная координата  нолика'))
          L[g][h] = "0"
          for j in range(4): print(*L[j])
          s += 1
          mot = True
          if victory(L):
              s= 11
              print('победа ноликов')
if s == 10  : print('Ничья')





