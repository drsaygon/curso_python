import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
bytes_html = response.content 
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

if parsed_html.title is not None:
    print(parsed_html.title.text)

texto_principal = parsed_html.select_one('body > main > p')
print(texto_principal.text)
