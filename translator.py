import requests
from http.client import responses
from bs4 import BeautifulSoup

while True:
    print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
    language = input()

    if language == 'fr' :
        language_url = 'english-french'
    else:
        language_url = 'french-english'

    print('Type the word you want to translate:')
    word = input()

    print(f'You chose "{language}" as a language to translate "{word}".')

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://context.reverso.net/translation/{language_url}/{word}'
    page = requests.get(url, headers=headers)

    print(f'{page.status_code} {responses[page.status_code]}')

    if page.status_code == 200:
        
        soup = BeautifulSoup(page.content,'html.parser')

        translations = soup.select("#translations-content .translation")
        translations_lst = []
        for t in translations:
            translations_lst.append(t.get_text().strip())

        
        sentences = soup.select("#examples-content .example .text")
        sentences_lst = []
        for e in sentences:
            sentences_lst.append(e.get_text().strip())

        print(translations_lst)
        print(sentences_lst)
        break
