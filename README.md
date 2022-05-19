# webscrapingG1.py
Web Scraping do noticiário G1 

# Sobre o Projeto
Desenvolvido durante estudos de Web Scraping. Este programa é capaz de fazer uma raspagem de dados dentro do site: https://g1.globo.com/, filtrar Notícia, Título e o Link e gerar um arquivo Excel contendo os dados coletados.

# Como Funciona? 
Para a construção deste programa seja possível, foi necessário a importação das Bibliotecas: Requests (responsável pelas solicitações HTTP), Bs4 (responsável pela raspagem de dados contidas na URL) e Pandas (responsável pela manipulação dos dados). Desta forma, a raspagem dos dados estará contida dentro de um laço For, para que haja a repetição do processo, tendo assim a coleta geral dos dados bem sucedida. Cada categoria filtrada, ficará armazenada em sua variável correspondente, facilitando a manipualação futura dos dados.

Após a coleta dos dados, é feito a chamada para a biblioteca Pandas, que será responsável pela criação do arquivo 'webscrapingG1-excel.xlsx', onde irá guardar todos os dados coletados, onde cada coluna representa a categoria filtrada e seus respectivos valores.

# Saída gerada

Conteúdo gerado em Excel pode ser visualizado e instalado em: https://github.com/Otavio1505/webscrapingG1.py/blob/main/webscrapinG1-excel.xlsx


# Autor
Otávio Moraes Braga
