import Alessandro

def readWebContent(urlToRead):
    return Alessandro.ReadWebPageContent(urlToRead)


def soluzione_01():
    s = ''.join([line.rstrip() for line in open('ocr.txt')])
    OCCURRENCES = {}
    for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
    avgOC = len(s) // len(OCCURRENCES)
    print
    ''.join([c for c in s if OCCURRENCES[c] < avgOC])  # equality



def soluzione_02():
    content = readWebContent(r"http://www.pythonchallenge.com/pc/def/ocr.html")
    textToFind = "find rare characters in the mess below"
    index = content.index(textToFind)
    textToSearch = content[index+len(textToFind):]

    occurrences = {}
    for c in textToSearch :
        occurrences[c] = occurrences.get(c,0) +1

    sequence = (c for c in textToSearch if occurrences[c] < 10)
    print("".join(sequence))


soluzione_02()