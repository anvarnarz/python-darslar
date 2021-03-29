from uzwords import words
def findMatches(word,words):	
	word = sorted(word)
	for lisso in words[1:]:
		for harf in lisso:			
			if word.count(harf) != list(lisso).count(harf) and word.count(harf)<list(lisso).count(harf):
				words.remove(lisso)
				break
			if harf not in (word):
				words.remove(lisso)
				break
	return words[1:]	     


print(findMatches('cтол', words))
print(findMatches('аломат',words))