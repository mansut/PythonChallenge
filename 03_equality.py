import Alessandro
import re

url = r"http://www.pythonchallenge.com/pc/def/equality.html"

content = Alessandro.ReadWebPageContent(url)
print(content)

pippo = content.replace('\\n',"")
print(pippo)

ale = re.findall("[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]",pippo)
print(''.join(ale))

#linkedlist :-)
#www.pythonchallenge.com/pc/def/linkedlist.php
#www.pythonchallenge.com/pcc/def/linkedlist.php