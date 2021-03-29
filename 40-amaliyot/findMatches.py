from uzwords import words
def isIn(text,word):
    toReturn = True
    word = list(word)
    for t in text:
        if t in word:
            word.remove(t)
        else:
            toReturn = False
    return toReturn

def findMatches(word,allWords=words):
    word = word.lower()
    matches = []
    for w in allWords:
        if len(w)<=len(word) and isIn(w,word) and w!=word:
            matches.append(w)
    return matches

if __name__ == "__main__":
    print(findMatches('олти', words))
    print(findMatches('аллома',words))
    print(findMatches('тараққиёт',words))