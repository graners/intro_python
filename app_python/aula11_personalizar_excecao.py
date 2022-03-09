# transformar toda nota que seja maior que 10 ou menor que 0 em uma exceção e se digitar algo que não seja número,
# também será exceção

# Por convenção, toda classe de erro tem que terminar com 'Error'
# Sempre que for criar uma classe personalizada de exceção, é necessário seguir a regra:
# Criar um classe chamada Error que herda de Exception e só então criar sua classe personalizada herdando da classe
# Error. A classe Error sempre deverá existir mesmo que não faça nada, só possua um pass.
class Error(Exception):  # uma classe chamada Erro que HERDA da classe Exception
    pass


class InputError(Error):  # Exceção personalizada
    def __init__(self, message):  # construtor
        self.message = message


while True:  # looping eterno enquanto não houver um break.
    try:
        nota = int(input('Digite uma nota de 0 até 10: '))
        if nota < 0 or nota > 10:
            # Utilizar o comando 'raise' para forçar uma exceção
            raise InputError('Valor inválido. Digite um valor entre 0 e 10.')
        print(nota)
        break  # se as linhas de código acima não derem erro, sai do while True
    except ValueError:
        print('Erro! Não é um número.')
    except InputError as ex:  # Tratando o erro para ser mais amigável ao usuário
        print(ex)
