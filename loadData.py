import re, json

def deEmojify(text):
    return text.encode('ascii', 'ignore').decode('ascii')


# Opening JSON file
fObj = open('People/Trump/trumpTweets.json',)

# It returns JSON object as dictionary
ogdata = json.load(fObj)
highestRT = ["", 0]


with open("trumpTweetsCleaned.txt","w+") as f:
    for i in ogdata:
        # print(i['text'])
        # print(i)

        if "https://" in i['text'] or "http://" in i['text']:
            httpRemoved = "" # i['text'][:i['text'].index("http")].strip()
        else:
            httpRemoved = i['text']

        if httpRemoved != "" and i['isRetweet'] == "f" :
            if i['retweets'] > 10000 and len(i['text']) < 125 and not i['text'].startswith("RT"):
                # print(i['retweets'], deEmojify(httpRemoved))
                f.write(deEmojify(httpRemoved) + "\n")

# Closing file
fObj.close()


