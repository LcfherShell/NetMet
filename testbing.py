from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, quote_plus

def search(query):
    address = "http://www.bing.com/search?q=%s" % (quote_plus(query))
    print(address)

    #getRequest = urllib.request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})

    urlfile = requests.get(address)
    htmlResult = urlfile.text
    #print(htmlResult)


    soup = BeautifulSoup(htmlResult, "html.parser")

    #[s.extract() for s in soup('span')]
    """unwantedTags = ['strong']
                for tag in unwantedTags:
                    for match in soup.findAll(tag):
                        match.replaceWithChildren()"""

    results = soup.findAll('li', { "class" : "b_algo" })
    for result in results:
            print("# TITLE: " + str(result.find('h2').text).replace(" ", " "))
            print("# LINK: " + str(result.find('a').attrs['href']).replace(" ", " "))
            print("# DESCRIPTION: " + str(result.find('p').text).replace(" ", " "))
            print("# ___________________________________________________________\n#")

    return results

if __name__=='__main__':
    links = search('Shakespeare')