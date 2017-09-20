import urllib.request as ur

def ReadWebPageContent(urlToRead) -> str:
    """
    Legge il contenuto di una pagina web
    :rtype: 
    :param urlToRead: indirizzo della pagina (stringa)
    :return: pagina (stringa)
    """
    f = ur.urlopen(urlToRead)
    return str(f.read())
