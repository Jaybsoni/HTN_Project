import os

# text = "This is a test. I want to see how this TEST will work. Poop Poop poop"
# text = (open("wonderland.txt").read().lower())


directory = "People/seuss/"
files = []
data = ""
text = ""
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(filename)
        with open (directory+filename, "r") as myfile:
            data = myfile.read().lower()                   #replace('\n', ' ')
        files.append(filename)
    text = text + data


# lower the string, split at spaces, remove extra grammar stuff
for i in ['.', ',', '!', '?', ';', '(', ')', '[', ']', '_', '-', '"', "'", '“', '…', '”', '‘', '’']:
    text = text.replace(i, "")

unique = list(set(text.split())) # make a list of only unique entries

# Adds special characters as their own elements
unique.extend(['.', ',', '!', '?', ';', '(', ')', '[', ']', '_', '-', '"', "'"])

unique.sort()
print(unique)

with open("seussWords.txt","w+") as f:
    for i in unique:
        f.write(i + "\n")