num_1 = int(input("Digite um número: "))
operacao = input("Digite a operação desejada: ")

if operacao != "√":
    num_2 = int(input("Digite o segundo número: "))

#Se o operador "+" for digitado, irá realizar a soma dos números digitados.
if operacao == "+":
    print(f"O resultado da soma é: {num_1 + num_2}" )

#Se o operador "-" for digitado, irá realizar a subtração dos números digitados.
elif operacao == "-":
    print(f"O resultado da subtração é: {num_1 - num_2}")

#Se o operador "*" for digitado, irá realizar a multiplicação dos números digitados.
elif operacao == "*":
    print(f"O resultado da multiplicação é: {num_1 * num_2}")

#Se o operador "/" for digitado, irá realizar a divisão dos números digitados.
elif operacao == "/":
    if num_2 == 0:
        print("Não é possivel dividir por zero.")        
    else:   
        print(f"O resultado da divisão é: {num_1 / num_2}") 

elif operacao == "√":
    import cmath
    raiz_quadrada = cmath.sqrt(num_1)
    if num_1 > 0 :
        import math
        raiz_quadrada = math.sqrt(num_1)
    print(f" O resultado da raiz quadrada é: {raiz_quadrada}")


elif operacao == "^":
    print(f"O resultado da exponenciação é: {num_1 ** num_2}")

elif operacao == "//":
    if num_2 == 0:
        print("Não é possivel dividir por zero.")
    else:
        print(f"O resultado da divisão inteira é: {num_1 // num_2}")

elif operacao == "%":
    print(f"O resto da divisão é: {num_1 % num_2}")

else:
    print("Syntax Error.")