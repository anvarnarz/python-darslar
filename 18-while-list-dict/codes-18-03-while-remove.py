"""
13/12/2020

Dasturlash asoslari

#18-dars: WHILE VA RO'YXATLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
cars = ["lacetti", "nexia", "toyota", "nexia", "audi", "malibu", "nexia", "lacetti"]
car = "lacetti"
while car in cars:
    cars.remove(car)

print(cars)
