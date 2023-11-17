"""
Original file is located at
    https://colab.research.google.com/drive/1o2f8Eh13GaZcnO4ULq>

#Web Scraping

É a técnica de extrair dados de websites. Nessa situação o seu >

O web scraping é permitido quando realizado em **dados públicos>

## Primeiros passos

Para começar, vamos pegar o conteúdo HTML de uma página Web.
"""
import requests
from bs4 import BeautifulSoup

# Endereço do site em que vamos fazer o scraping
url = 'https://tribunademinas.com.br/noticias/regiao'

# Realiza uma conexão ao site acima, obtendo uma resposta
response = requests.get(url)

# Verifica se a conexão foi bem-sucedida
if response.status_code == 200:
    # Obtém o código HTML do site
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    # Procura por <h2> dentro do HTML

    all_h2 = soup.find_all("h2")
    for h2 in all_h2:
        print(h2.text)
    '''
    start_index = soup.find('div', class_='row')

    coluna = start_index.find('div', class_='col-sm-8')
    linhas = coluna.find_all('div', class_='col-sm-8')
    for a in linhas:
        
        h2 = a.find_all('h2')
        manchete = [h2.text]

    for m in manchete:
        print(m)
    '''
'''
# Encontra o final da tag </h2>
end_index = html_content.find('</h2>')

# "Pega" a parte do HTML que está entre o começo e o fim de title, ou seja, <title> </title>
h2 = html_content[start_index:end_index]

print("A manchete do site é:", h2)'''
