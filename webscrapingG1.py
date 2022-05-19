import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get("https://g1.globo.com/")

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    titulo2 = noticia.find('a', attrs={'class': 'feed-post-link'})
    titulo1 = noticia.find('span', attrs={'class': 'feed-post-header-chapeu'})
    if (titulo1):
        lista_noticias.append([titulo1.text, titulo2.text, titulo2["href"]])

news = pd.DataFrame(lista_noticias, columns=['Noticia', 'Titulo', 'Link'])

news.to_excel('webscrapinG1-excel.xlsx', index=False)
print(news)
