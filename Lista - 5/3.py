#numero de primos e divisões
num = int(input("Digite um número: "))
primos=[]
i=0
for nu in range(1,num+1):
    for n in range(1 , nu+1):
        i=i+1
        if nu % n == 0 and n!=1 and n!=nu:
            break
        elif nu == n:
            primos.append(nu)

print(f"Esses são os numero primos que existem entre 1 e {num}: {primos}")
print(f'E foram feitas {i} divisões')