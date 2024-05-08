print("Tabela de preços:")
for i in range(1, 11):
    espaco_extra = " " if i <= 5 else ""
    print(f"{i:2} - R${i*1.99:.2f}",
          f"{espaco_extra}| {i+10:2} - R${(i+10)*1.99:.2f} "
          f"| {i+20:2} - R${(i+20)*1.99:.2f} "
          f"| {i+30:2} - R${(i+30)*1.99:.2f} "
          f"| {i+40:2} - R${(i+40)*1.99:.2f}")
