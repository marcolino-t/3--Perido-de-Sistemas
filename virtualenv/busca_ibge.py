from flask import Flask, request
from ibge import busca, calcula_ocorrencia,calcula_maior_frequencia,calcula_menor_frequencia

app = Flask(__name__)

#http://127.0.0.1:5000/busca_nome?nome=jose
@app.route("/busca_nome")
def busca_rota():
    try:
        nome = request.args.get('nome')
        response = busca(nome)
        total_ocorrencia = calcula_ocorrencia(response)
        maior_frequencia = calcula_maior_frequencia(response)
        menor_frequencia = calcula_menor_frequencia(response)

        # Criar um dicionário com as informações formatadas
        resposta = {
            "nome_procurado": nome,
            "total_ocorrencia": total_ocorrencia,
            "maior_frequencia": maior_frequencia,
            "menor_frequencia": menor_frequencia
        }
    
        return resposta
    

    
    
    except Exception as e:
        return(f"falha na tora: {e}")
    
app.run(debug=True)    