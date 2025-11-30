#Irá pedir para digitar um número.
num_1 = int(input("Digite um número: "))
#Irá perguntar qual operação deseja realizar.
operacao = input("Digite a operação desejada: ")

#Essa condição será realizada, quando o operador digitado seja dirente de "√"
if operacao != "√":
    #Se a condição acima for aceita, irá aparecer a opção de você digitar o segundo número.
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
#Se o operador "√" for digitado, irá realizar a raiz quadrada do número digitado.
elif operacao == "√":
    import cmath
    raiz_quadrada = cmath.sqrt(num_1)
    if num_1 > 0 :
        import math
        raiz_quadrada = math.sqrt(num_1)
    print(f" O resultado da raiz quadrada é: {raiz_quadrada}")

#Se o operador "^" for digitado, irá realizar a potenciação dos números digitados.
elif operacao == "^":
    print(f"O resultado da potenciação é: {num_1 ** num_2}")

#Se o operador "//" for digitado, irá realizar a divisão inteira dos números digitados.
elif operacao == "//":
    if num_2 == 0:
        print("Não é possivel dividir por zero.")
    else:
        print(f"O resultado da divisão inteira é: {num_1 // num_2}")

#Se o operador "%" for digitado, irá pegar o resto da divisão da divisão que foi realizada com os números digitados.
elif operacao == "%":
    print(f"O resto da divisão é: {num_1 % num_2}")

#Se nenhuma das codições acima for ativada, irá aparecer esse resultado de "Error".
else:
    print("Syntax Error.")

