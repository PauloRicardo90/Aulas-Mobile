def somar_e_verificar_paridade(num1, num2):
    # Somar os dois números
    soma = num1 + num2
    
    # Verificar se a soma é par ou ímpar
    if soma % 2 == 0:
        print("A soma de", num1, "e", num2, "é", soma, "e é par.")
    else:
        print("A soma de", num1, "e", num2, "é", soma, "e é ímpar.")

# Exemplo de utilização
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

somar_e_verificar_paridade(num1, num2)
