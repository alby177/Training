import requests, os, bs4

url = 'https://forum.codesys.com/viewtopic.php?f=11&t=8852'
os.makedirs('codesysForum', exist_ok = True) # Crea una cartella codesysForum
str = ''
while True:

    print("Dowloading page {}...".format(url))
    res = requests.get(url, headers={'user-agent' : 'Mozilla/5.0'})
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    forumElems = soup.select('div.postbody') # Seleziona la classe postbody tra i tag div

    if forumElems == []:
        print('Nothing to save!')
    else:
        for i in forumElems:
            str = str + i.getText() + '\n\n'
    try:
        nextPage = soup.find("a", string="Next") # trova la stringa "Next" cercando tra gli elementi a della pagina parsed
        NPLink = nextPage['href'] # per l'elemento che ritorna il metodo .find, trova la parte corrispondente ad href e la fa diventare una stringa
        url = 'https://forum.codesys.com' + NPLink[1:]
    except TypeError:
        break

topicName = soup.find("a", class_="titles").getText()
forumFile = open(os.path.join('codesysForum', topicName + '.txt'), 'w')
forumFile.write(str)
forumFile.close()
print('Done!')


#if soup.find("div", class_="quotecontent") is not None: # Trova la classe quotecontent all'interno del tag div
    #print(soup.find("div", class_="quotecontent"))
