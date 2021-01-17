import os
import re
#
directory = "People/seuss/"
files = []
data = ""
text = ""
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open (directory+filename, "r") as myfile:
            data = myfile.read().lower()                   #replace('\n', ' ')
        files.append(filename)
    text = text + data


text = (open("wonderland.txt").read().lower())
extras = ['.', ',', '!', '?', ';', '(', ')', '[', ']', '_', '-', '"', "'",]

for i in extras:
    text = text.replace(i, f" {i} ")
separatedText = text.split()

# lower the string, split at spaces, remove extra grammar stuff
for i in extras:
    text = text.replace(i, "")

# Remove dirty ones
for i in ['“', '…', '”', '‘', '’']:
    text = text.replace(i, "")

unique = list(set(text.split())) # make a list of only unique entries

# Adds special characters as their own elements
unique.extend(extras)

unique.sort()
# print(unique)

with open("seussWords.txt","w+") as f:
    for i in unique:
        f.write(i + "\n")




text = (open("wonderland.txt").read().lower())
for i in extras:
    text = text.replace(i, f" {i} ")
separatedText = text.split()






# # LESSION TO BE LEARNT HERE
# # corect
# In [5]: for i in extras:
#    ...:     strr = strr.replace(i, f" {i} ")
#    ...: strr.split()
#
#
# # baddd
# def seperate(word, extras, listToAdd):
#     print("-------WORD IS", word)
#     for eachExtra in extras:
#         if eachExtra in word:
#
#             print(f"---word is -{word}-, and each Extra is -{eachExtra}-")
#             first, second = word.split(eachExtra, 1)
#             print(f"first is -{first}- and -{second}-")
#
#             if first == "":
#                 print(f"appending just {eachExtra}")
#                 listToAdd.append(eachExtra)
#             else:
#                 print(f"appending {first} and {eachExtra}")
#                 listToAdd.append(first)
#                 listToAdd.append(eachExtra)
#
#             seperate(second, extras, listToAdd)
#
#     # if not any(x in word for x in Extras):
#     #     listToAdd.append(word)
#
# strs = ['hello', 'world.', 'cat."']
# print(strs)
# Extras = ['.', '"']
# # Extras = ['"', '.']
# newStrs = []
# for word in strs:
#     if not any(x in word for x in Extras):
#         newStrs.append(word)
#     else:
#         seperate(word, Extras, newStrs)
#
# print(newStrs)
