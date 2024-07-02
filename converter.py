from PIL import Image
import os, re, pillow_avif

dirInput = input("submit directory: \n")
os.chdir(dirInput)
files = os.listdir(dirInput)
fileDict = {}

for file in files:
    match = re.search("[.][a-zA-Z]+$", file)
    if(match == None):
        continue
    filetype = match.group()
    if filetype in fileDict:
        fileDict.update({filetype: fileDict.get(filetype) + 1})
    else:
        fileDict[filetype] = 1

print("found the following image types in the directory: ")
print(fileDict)

def fun(file):
    if(file.endswith(convertTarget)):
        return True
    else:
        return False

convertTarget = input("submit the filetype to convert: \n")
filesToConvert = filter(fun, files)
targetInput = input("submit the output file format: \n (1) jpg \n (2) png \n")
targetType = None

if(targetInput == "1"):
    targetType = ".jpg"
elif(targetInput == "2"):
    targetType = ".png"

removeOldInput = input("remove old files? (leave empty for yes) \n (n) No \n")
removeOld = True
if(removeOldInput == "n"):
    removeOld = False

print("converting the following files to " + targetType + ": ")
for i in filesToConvert:
    print(i)
    im = Image.open(i)
    rgb_im = im.convert("RGB")
    filename = i.rstrip(convertTarget)
    newFilename = filename + targetType
    rgb_im.save(newFilename)
    if(removeOld):
        os.remove(i)
print("all files converted")