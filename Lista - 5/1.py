# 1- numero é primo 
num = int(input("Digite um número: "))
for nu in range(1 , num+1):
    if num % nu == 0 and nu!=1 and nu!=num:
        print(f"O Número {num} não é primo")
        break
    elif num == nu:
        print(f"O Número {num} é primo")
