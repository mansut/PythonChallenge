import re
import zipfile

zipFileName = r"D:\Documenti\A - Studio\Python\pythonchallenge\zip\channel.zip"
zipObj = zipfile.ZipFile(zipFileName)
print(zipObj)
infoList = zipObj.infolist()
for i in infoList:
    print(i.comment)


# zipDir = r"D:\Documenti\A - Studio\Python\pythonchallenge\zip\\"
# startingNumer = 90052
#
# while True:
#     fileName = zipDir + str(startingNumer) + ".txt"
#     f = open(fileName)
#     line = f.read()
#     match = re.search("Next nothing is (\d+)",line)
#     if (match == None) : break
#     startingNumer = match.group(1)
#     print(startingNumer)


