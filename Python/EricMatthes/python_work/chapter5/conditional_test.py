cars = ['bmw', 'audi', 'skoda', 'mazda', 'fiat']
for car in cars:
    if car == 'bmw' or car == 'fiat':
        print(car.upper())
    else:
        print(car.title())
emmploers_ITMO = ['lera', 'nikita', 'iliya', 'filipp', 'ivan']
emmploer = 'lera'
if emmploer in emmploers_ITMO:
    print("You are welcome to ITMO uneversity")
else:
    print("Go away from here!!!")

