entrada1 = input("Qual seu nome? ")
print("Olá, " + entrada1 + "!")
entrada2 = int (input("Qual sua idade? "))
if entrada2 >= 18:
    print("Você é maior de idade.")
elif entrada2 < 18 and entrada2 >= 0:
    print("Você é menor de idade.")
else:
    print("Digite um valor válido!")