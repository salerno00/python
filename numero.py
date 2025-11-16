letra = 's'

while letra == 's':

    numero = []

    i=0
    while i < 15:
        n = int(input(f"Digite o {i+1}º número: "))
        if n in numero:
            print("Não repita números!!")
        else:
            numero.append(n) 
            i += 1   
    numero.sort()
        
    pares = sum(1 for n in numero if n % 2 == 0)
    impares = 15 - pares
    soma = sum(numero)
    media = soma/15
    maior = max(numero)
    menor = min(numero)

    print("\nOrdem crescente dos numeros: ")
    print(numero)
    print("\nQuantidade de numeros pares: ",pares)
    print("\nQunatidade de numeros impares: ",impares)
    print("\nSoma de todos os números: ",soma)
    print("\nA média desses números é: ",media)
    print("\nO maior número é:  ",maior)
    print("\nO menor numero é: ",menor)

    letra = input("Usar novamente(s/n) ")