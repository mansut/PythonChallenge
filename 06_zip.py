import re
import zipfile

zipFileName = r"D:\Documenti\A - Studio\Python\pythonchallenge\zip\channel.zip"
zipObj = zipfile.ZipFile(zipFileName)
startingNumer = 90052

comments = []

while True:
    fileName = str(startingNumer) + ".txt"
    info = zipObj.getinfo(fileName)
    comments.append(info.comment.decode())  # Da bytearray a stringa (encode <--> decode)
    line = zipObj.read(fileName).decode()
    match = re.search("Next nothing is (\d+)",line)
    if (match == None) : break
    startingNumer = match.group(1)

print("".join(comments))

# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************

#oxygen