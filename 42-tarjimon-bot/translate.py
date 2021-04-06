from googletrans import Translator

def translate(matn):
    translator = Translator()
    # matn tilini aniqlaymiz
    til = translator.detect(matn).lang    
    if til=='en': # agar til ingliz tilda boʻlsa
        return translator.translate(matn,dest='uz').text
    else:
        return translator.translate(matn,dest='en').text