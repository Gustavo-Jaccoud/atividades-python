# 2 - se numero não é primo quais são os divisores
num = int(input("Digite um número: "))
div = []
for nu in range(1 , num+1):
    if num % nu == 0:
        div.append(nu)

if len(div) > 2:
    print(f' N é primo e é divisivel por {div}')
else:
    print('É primo')