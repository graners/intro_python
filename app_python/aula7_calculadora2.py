class Calculadora:
    # se não quiser inicializar com valores
    # porém, não pode ficar vazio, então coloca 'pass' que é para fazer nada
    # Também é possível tirar o init que vai funcionar igual porque não haverá inicialização com parâmetros
    def __init__(self):
        pass

    # Como os métodos estão dentro de uma classe, eles terão de usar o self para acessar os valores da classe
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return 'Erro: divisão por zero.'


# Instanciando uma classe:
calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 6))
print(calculadora.multiplicacao(7, 9))
print(calculadora.divisao(5, 3))
