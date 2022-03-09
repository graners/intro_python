import requests


def retorna_dados_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)  # valor do status de retorno: 200 Ok, 400 Erro
    print(response.text)  # imprime o "texto da página", ou seja, o JSon
    print(type(response.text))
    print(response.json())  # retorna o json em formato de dicionário
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])


def retorna_dados_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    # retorna_dados_cep('69103-256')
    # info_pokemon = retorna_dados_pokemon('pikachu')
    # print(info_pokemon)
    # print(info_pokemon['sprites']['front_shiny'])
    res = retorna_response('https://www.metasistemas.com.br/')
    print(res)
