def contar_digitos(numero):
    return len(str(numero))

def calcular_cvc(numero):

    lista_multiplicacao = []
    lista_outros = []
    numero = 0
    indice = 1
    soma = 0

    for i in range(16):
        numero = (numero // 10**i) % 10
        if indice % 2 == 0:
            
            lista_multiplicacao.append(numero*2)
        else:
            lista_outros.append(numero)
        indice+=1

    for j in range(len(lista_multiplicacao)):
        if lista_multiplicacao[j] > 9:
            n1 = lista_multiplicacao[j] % 10
            n2 = lista_multiplicacao[j] // 10
            lista_multiplicacao[j] = 0
            lista_multiplicacao.append(n1)
            lista_multiplicacao.append(n2)
            soma = sum(lista_multiplicacao)
        else:
            soma = sum(lista_multiplicacao)

    lista_outros.append(soma)
    cvc = sum(lista_outros)
    return cvc

def verificar_cartao(numero):
    digitos = contar_digitos(numero)

    if digitos not in [13, 15, 16]:
        print("INVALID")
        return

    cvc = calcular_cvc(numero)

    card_type = "INVALID"

    if str(numero)[0] == '3' and str(numero)[1] in ['4', '7']:
        card_type = "AMEX"

    elif str(numero)[0] == '5' and str(numero)[1] in ['1', '2', '3', '4', '5']:
        card_type = "MASTERCARD"

    elif str(numero)[0] == '4':
        card_type = "VISA"

    if cvc % 10 != 0:
        return ("INVALID")
    else:
        return (card_type)
