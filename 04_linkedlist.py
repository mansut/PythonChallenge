import urllib
import Alessandro
import re

rawAddress = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def completeAddress(value):
    return rawAddress + str(value)

currentAddress = completeAddress(0)

while True:
    text = Alessandro.ReadWebPageContent(currentAddress)
    print(text)
    m = re.search("and the next nothing is (\d+)",text)
    if m == None : break
    print(m.group(1))
    currentAddress = completeAddress(m.group(1))

#peak.html :-)

#www.pythonchallenge.com/pc/def/peak.html
#www.pythonchallenge.com/pcc/def/peak.html