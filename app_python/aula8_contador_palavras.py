def contador_letras(lista_palavras):
    contador = []
    for palavra in lista_palavras:
        quantidade = len(palavra)
        contador.append(quantidade)
    return contador


def teste():
    return 'teste'


if __name__ == '__main__':
    print(contador_letras(['Bruna', 'Maria', 'Beatriz', 'Catarina']))
