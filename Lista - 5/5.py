perguntas=["Telefonou para a vítima?", "Esteve no local do crime?",
"Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas=0
for pergunta in perguntas:
    resposta = str(input(f'{pergunta} (Sim/Não): '))
    if resposta.lower() == 'sim':
        respostas = respostas + 1
match respostas:
    case 2:
        print("Suspeita")
    case 3:
        print("Cúmplice")
    case 4:
        print("Cúmplice")
    case 5:
        print("Assassino")
    case _:
        print("Inocente")

