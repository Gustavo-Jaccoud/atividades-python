#Calculo fatorial
num = int(input("Digite um número: "))
fatorial = num
for nu in range(1 , num):
    fatorial = fatorial *(num-nu)
print(f'o fatorial de {num} é: {fatorial}')
    
