unconfirmeds = ['tanya', 'liza', 'katay']
confirmes = []

while unconfirmeds:
    current = unconfirmeds.pop()

    print("\nVerifying user: " + current.title())
    confirmes.append(current)

print("\nThe following users have been confirmed: ")
for confirmed in confirmes:
    print(confirmed.title())
