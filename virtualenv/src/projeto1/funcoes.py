import requests
import unicodedata

def lista_Cidades(): #função criada para extrair json() da api
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos" #url que será extraido meu arquivo json
    resposta = requests.get(url) #variavel 'resposta' armazena minha requisição na url do ibge
    return resposta.json() #o retorno e tranformado em formato json



def sigla(UF): #função criada com parametro
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/distritos"#Url que pede um parametro que no caso é o parametro UF que falta
    resposta = requests.get(url)  #variavel 'resposta' armazena minha requisição na url do ibge
    return resposta.json()  #o retorno e tranformado em formato json


def ordenar_cidades(cidades): #função para ordenar
    nomes_cidades=[]
    for cidade in cidades:  # Iterar sobre cada cidade na lista de cidades
        nome = cidade['nome']  # Obter o nome da cidade
        # Normalizar o nome removendo acentos e caracteres especiais
        nome_normalizado = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
        nomes_cidades.append(nome_normalizado)  # Adicionar o nome normalizado à lista de nomes de cidades
    return nomes_cidades  # Retornar a lista de nomes de cidades normalizados
