import shutil  # por convenção, colocar os imports no início do módulo

# Criar um arquivo

# utilizando um built-in do python
# se já existir um arquivo com esse nome, não será criado outro
# arquivo = open('teste.txt', 'w')  # nome do arquivo e extensão, w (de write)
# arquivo.write('minha primeira escrita')  # adiciona/sobrepoe conteúdo quando tiver 'w' no open()
# arquivo.close()

# caso queira só acrescentar mais conteúdo sem perder o anterior, utilizar 'a' no open()
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nminha primeira escrita linha 2')
# arquivo.close()

def escrever_arquivo(texto):
    diretorio = 'C:/Users/steff/Downloads/teste.txt'  # gerando arquivo no diretório desejado
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')  # quando não passa caminho de diretório, ele salva no diretório atual em que o
#     # python está sendo executado
#     arquivo.write(texto)
#     arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    lista_alunos = arquivo.read().split()
    print(lista_alunos)
    lista_media = []
    for aluno in lista_alunos:
        aluno_nota = aluno.split(',')
        aluno = aluno_nota[0]
        aluno_nota.pop(0)
        media = lambda notas: sum([int(i) for i in aluno_nota]) / 4
        print(f'A média do(a) aluno(a) {aluno} é {media(aluno_nota)}')
        lista_media.append({aluno: media(aluno_nota)})
    return lista_media


def copia_arquivo(nome_arquivo):
    # import shutil
    shutil.copy(nome_arquivo, 'C:/Users/steff/Downloads/medias2.txt')


def mover_arquivo(nome_arquivo, local):
    # import shutil
    shutil.move(nome_arquivo, local)


if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Segunda linha.')
    # ler_arquivo('teste.txt')
    # aluno = '\nCesar,9,9,2,4'
    # atualizar_arquivo('notas.txt', aluno)
    # lista_medias = str(media_notas('notas.txt'))
    # print(type(lista_medias))
    # atualizar_arquivo('medias.txt', lista_medias)
    # ler_arquivo('medias.txt')
    # copia_arquivo('medias.txt')
    mover_arquivo('medias.txt', 'C:/Users/steff/Documents')
