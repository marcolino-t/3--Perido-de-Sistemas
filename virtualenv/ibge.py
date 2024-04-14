import requests

def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json()

def calcula_ocorrencia(var_json):
    conteudo = var_json[0]
    resposta = conteudo.get('res',[])
    soma = []
    for elemento in resposta:
        frequencia = elemento.get('frequencia',0)
        soma.append(frequencia)

    return sum(soma)

def calcula_maior_frequencia(var_json):
    conteudo = var_json[0]
    resposta = conteudo.get('res',[])
    maior_frequencia = 0
    ano_maior_frequencia = None  # Inicialize o ano com None
    for elemento in resposta:
        frequencia = elemento.get('frequencia', 0)
        ano = elemento.get('periodo', None)  # Obtenha o ano do elemento
        if frequencia > maior_frequencia:
            maior_frequencia = frequencia
            ano_maior_frequencia = ano  # Atualize o ano correspondente à maior frequência

    return maior_frequencia, ano_maior_frequencia
  
def calcula_menor_frequencia(var_json):
    conteudo = var_json[0]
    resposta = conteudo.get('res',[])
    menor_frequencia = 2024
    ano_menor_frequencia = None  # Inicialize o ano com None
    for elemento in resposta:
        frequencia = elemento.get('frequencia', 0)
        ano = elemento.get('periodo', None)  # Obtenha o ano do elemento
        if frequencia < menor_frequencia:
            menor_frequencia = frequencia
            ano_menor_frequencia = ano  # Atualize o ano correspondente à menor frequência

    return menor_frequencia, ano_menor_frequencia
  
    