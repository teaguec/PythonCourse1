names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names.extend(names1)

for index in range(2):
    names.append(input("Enter new name "))
for name in names:
    print(f"{name.title()}! You are invited to the party on Saturday.")
    