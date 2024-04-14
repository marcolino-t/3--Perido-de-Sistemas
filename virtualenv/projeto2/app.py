from flask import Flask, request
from defs import lista_Cidades, nomes, quick_sort, merge_sort, bubble_sort, selection_sort, insertion_sort
import time

# Instanciar a aplicação
app = Flask(__name__)

# Rota para retornar todas as cidades do IBGE
@app.route("/lista_ibge")
def Todas_cidades(): # Obter a lista de cidades
    cidades = lista_Cidades() # Extrair apenas os nomes das cidades
    nomes_cidades = nomes(cidades) # Retornar os nomes das cidades
    return nomes_cidades

# Rota para ordenar as cidades usando Quick Sort
@app.route("/quick_ibge")
def OrdQuick(): # Iniciar a contagem do tempo de execução
    inicio = time.time() # Obter a lista de cidades
    cidades = lista_Cidades() # Ordenar as cidades usando Quick Sort
    quick_sort(cidades) # Extrair apenas os nomes das cidades
    nomes_cidades = nomes(cidades) # Finalizar a contagem do tempo de execução
    fim = time.time() # Calcular o tempo de execução
    tempo_execucao = fim - inicio # Imprimir o tempo de execução
    print(f"Tempo de execução da rota /quick_ibge: {tempo_execucao} segundos") 
    return nomes_cidades # Retornar os nomes das cidades

# Rota para ordenar as cidades usando Merge Sort
@app.route("/merge_ibge")
def OrdMerge(): # Iniciar a contagem do tempo de execução
    inicio = time.time() # Obter a lista de cidades
    cidades = lista_Cidades() # Extrair apenas os nomes das cidades
    nomes_cidades = nomes(cidades) # Ordenar as cidades
    merge_sort(0, len(nomes_cidades), nomes_cidades) # Finalizar a contagem do tempo de execução
    fim = time.time() # Calcular o tempo de execução
    tempo_execucao = fim - inicio # Imprimir o tempo de execução
    print(f"Tempo de execução da rota /merge_ibge: {tempo_execucao} segundos") 
    return nomes_cidades # Retornar os nomes das cidades

# Rota para ordenar as cidades usando Bubble Sort
@app.route("/bubble_ibge")
def OrdBubble(): # Iniciar a contagem do tempo de execução
    inicio = time.time() # Obter a lista de cidades
    cidades = lista_Cidades() # Extrair apenas os nomes das cidades
    nomes_cidades = nomes(cidades) # Ordenar as cidades usando Bubble Sort
    bubble_sort(nomes_cidades) # Finalizar a contagem do tempo de execução
    fim = time.time() # Calcular o tempo de execução
    tempo_execucao = fim - inicio # Imprimir o tempo de execução
    print(f"Tempo de execução da rota /bubble_ibge: {tempo_execucao} segundos") 
    return nomes_cidades # Retornar os nomes das cidades

# Rota para ordenar as cidades usando Selection Sort
@app.route("/selection_ibge")
def OrdSelection(): # Iniciar a contagem do tempo de execução
    inicio = time.time() # Obter a lista de cidades
    cidades = lista_Cidades() # Extrair apenas os nomes das cidades
    nomes_cidades = nomes(cidades) # Ordenar as cidades usando Selection Sort
    selection_sort(nomes_cidades) # Finalizar a contagem do tempo de execução
    fim = time.time() # Calcular o tempo de execução
    tempo_execucao = fim - inicio # Imprimir o tempo de execução
    print(f"Tempo de execução da rota /selection_ibge: {tempo_execucao} segundos") 
    return nomes_cidades # Retornar os nomes das cidades

# Rota para ordenar as cidades usando Insertion Sort
@app.route("/insertion_ibge")
def OrdInsertion(): # Iniciar a contagem do tempo de execução
    inicio = time.time() # Obter a lista de cidades
    cidades = lista_Cidades() # Extrair apenas os nomes das cidades
    nomes_cidades = nomes(cidades) # Ordenar as cidades usando Insertion Sort
    insertion_sort(nomes_cidades) # Finalizar a contagem do tempo de execução
    fim = time.time() # Calcular o tempo de execução
    tempo_execucao = fim - inicio # Imprimir o tempo de execução
    print(f"Tempo de execução da rota /insertion_ibge: {tempo_execucao} segundos") 
    return nomes_cidades # Retornar os nomes das cidades

if __name__ == "__main__":
    app.run(debug=True)
