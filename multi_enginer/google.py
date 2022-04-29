from bs4 import BeautifulSoup

def Google(search):
    results = []
    texts = []
    soup = BeautifulSoup(search, 'html.parser')
    for i in soup.find_all('div', {'class' : 'kCrYT'}):
            links = i.find_all('a')
            link_text = i.find('h3')
            results.append(links)
            texts.append(link_text.text)
 
    return(texts, results)