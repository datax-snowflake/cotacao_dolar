import requests
import urllib.request
import datetime

# Configuracao da URL
url = "https://br.investing.com/currencies/usd-brl"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

req = urllib.request.Request(url, headers=headers)

# Faz a requisição à página
response = urllib.request.urlopen(req)
html_bytes = response.read()
html = html_bytes.decode("utf-8")
hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Extração de texto
prefix = '<span class="text-2xl" data-test="instrument-price-last">'
suffix = "</span>"
prefix_hora = '<time class="instrument-metadata_text__Y52j_ font-bold" dateTime="'
suffix_hora = "</time>"

# Encontra a posição do texto antes e depois do valor
start = html.find(prefix) + len(prefix)
end = html.find(suffix, start)
start_hora = html.find(prefix_hora) + len(prefix_hora)
end_hora = html.find(suffix_hora, start_hora)


# Extrai o valor
valor = html[start:end]
hora = html[start_hora:end_hora]
saida_UTC = hora.split('">', 1)[0]
saida_BR = hora.split('">', 1)[1]

saida_UTC = datetime.datetime.strptime(saida_UTC, "%Y-%m-%dT%H:%M:%S.%fZ").strftime(
    "%Y-%m-%d %H:%M:%S"
)


#print(
 #   "\n",
 #   "Horário atual:",
 #   hora_atual,
 #   "\n",
 #   "Horário UTC:",
 #   saida_UTC,
 #   "\n",
 #   "Horário Brasília:",
 #   saida_BR,
 #   "\n",
 #   "Cotação:",
 #   valor,
#)


#UTC_timezone

streamlit.header("Cotação do dólar")
streamlit.text(saida_utc)
streamlit.text(valor)
