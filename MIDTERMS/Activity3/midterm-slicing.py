#!/usr/bin/env python3
#Author: Alex Kunze, Purpose: Slicing and Dicing Strings

print("Name: Alex Kunze")

openFile = open("slicing-file.txt", "r")
openFyle = openFile.readlines()


aVar = openFyle[-3]
bVar = openFyle[2:5]
cVar = openFyle[-10:-16:-2]
dVar = openFyle[10:13]
eVar = openFyle[-19:-22:-1]

quote = str(aVar + "".join(bVar) + "".join(cVar) + "".join(dVar) + "".join(eVar))
I_am = quote.split(" ")
Going_Mad = str(I_am)
print(Going_Mad.replace("\\n", " ").replace("[", "").replace("]", "").replace(". ", "."))
openFile.close()
