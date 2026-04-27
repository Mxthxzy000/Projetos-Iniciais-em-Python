nome = input("Qual seu nome? ")
altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura * altura)
print("Olá, " + nome + "! O seu IMC é: " ,  imc) 
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 24.9:
    print("Voce esta no peso ideal.")
elif imc >= 25 and imc < 29.9:
    print("Voce esta com sobrepeso.")
elif imc >= 30 and imc < 34.9:
    print("Voce esta com obesidade I.")
elif imc >= 35 and imc < 39.9:
    print("Voce esta com obesidade II.")
else:
    print("Voce esta com obesidade III.")