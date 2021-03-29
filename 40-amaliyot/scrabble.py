from uzwords import words
from isIn import isIn
import random

word = words[random.randint(0,len(words))]
print("Tasodifiy so'z:", word)
print("Harflar: ", sorted(list(word)))

for w in words:
    if len(w)<=len(word) and isIn(w,word):
        print(w)


                
    
