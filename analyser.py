import os

#print(*os.listdir("./opinons")) #wyświetlanie plików w folderze
print(*[filename.split(".")[0] for filename in os.listdir("./opinons")],sep="\n")