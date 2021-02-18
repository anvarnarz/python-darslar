import json
files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']

for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)        
    except FileNotFoundError:
        print(f"{filename} fayli mavjud emas")
        #pass
    else:
        print(talaba['ism'])
        # fayl ustida turli amallar 