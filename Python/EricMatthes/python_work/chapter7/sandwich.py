sandwich_orders = ['good','pastami','bad','pastami','so-so','pastami','tuna_sandwich']
finishid_sandwiches = []

while 'pastami' in sandwich_orders:
    sandwich_orders.remove('pastami')
print("All 'pastami was delete from list'")
while sandwich_orders:
    current = sandwich_orders.pop()
    print("I made your " + current + " sandwich")
    finishid_sandwiches.append(current)
print("The folowing sanndwiches transfer in different list: ")
for transfer in finishid_sandwiches:
    print(transfer)