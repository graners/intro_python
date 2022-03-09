# EXCEÇÕES
# Docs: https://docs.python.org/3/library/exceptions.html

lista = [1, 3]
arquivo = open('teste.txt', 'r')
try:
    divisao = 10 / 1
    # lista[3]
    # x = a
    print(arquivo.read())
    arquivo.close()  # se der erro nas linhas anteriores, o arquivo não fechará
# # Tomar cuidado com a hierarquia das exceções: especificar filhas antes de pais
# except ZeroDivisionError:  # ZeroDivisionError é uma classe builtin do Python
#     print('Divisão por zero: operação inválida.')
# except:  # tratamento de erro genérico
#     print('Erro desconhecido')
except ArithmeticError as ae:
    print(f'Houve um erro aritmético: {ae}')
except IndexError:
    print('Índice inválido')
    # grava a mensagem de erro como 'ex':
# except BaseException as ex:  # Todas as exceções possuem 'pai' e 'filho'. BaseException é o pai de todas as exceções
#     # se não ocorrer nenhuma das outras exceções especificadas acima, cai nesta
#     print(f'Erro desconhecido. Erro: {ex}.')
except Exception as ex:  # É filha de BaseException. Exceções que mais acontecem tem Exception como pai
    print(f'Erro desconhecido. Erro: {ex}.')
# Utilizar else quando um bloco de código precisa ser executado após verificar que não houve qualquer erro:
else:
    print('Executa quando não tem exceção.')
finally:
    print('Sempre executa, independente de ocorrer erro.')
    arquivo.close()  # isso garante que mesmo que tenha dado erro no try, o arquivo será fechado
