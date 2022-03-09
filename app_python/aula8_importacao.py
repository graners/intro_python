from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_palavras import contador_letras, teste  # importando mais de uma coisa

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.canal)
    print(televisao.ligada)
    televisao.power()

    # para funcionar, acrescentar: <if __main__ == '__main__':> no módulo aula7_calculadora1
    calculadora = Calculadora(8, 9)
    print(calculadora.soma())

    lista = ['Abacate', 'Mamão', 'Pera', 'Laranja']
    # como não é uma classe, não precisa instânciar
    print(contador_letras(lista))
    
    print(teste())
