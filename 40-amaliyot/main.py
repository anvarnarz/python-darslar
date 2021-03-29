from uzwords import words
from findMatches import findMatches
import random

# uzwors.py ichidan 1 tasodifiy so'z tanlaymiz
word = words[random.randint(0,len(words))]
print("Тасодифий сўз:", word)
print("Ҳарфлар: ", sorted(list(word)))

matches = findMatches(word,words)

print("Топилган сўзлар:", sorted(matches,key=len,reverse=True))


                
    
