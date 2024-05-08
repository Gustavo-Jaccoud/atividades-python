#Fibonacci
num = int(input("Digite um número: "))
fibonacci = [0, 1]  # Começamos com os dois primeiros termos da sequência

while len(fibonacci) < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)