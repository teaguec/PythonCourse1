#THIS WAS UP TO AND INCLUDING "Lists - Exercise" video

#PART 1
print("Welcome!")
name = input("Enter name")
age = int(input("Enter age"))
money = float(input("enter balance"))

print("=====SUMMARY=====")
print(name.upper())
print(age + 1)
print(f"your balance is: £{money:.2f}")


#PART 2
username_1 = name[0:3]
username_2 = name[-2:]
username = username_1 + username_2
print(username)

new_name = name.replace(" ", "_")
print(new_name)
print(len(new_name))
fav_game = input("what is your fav game")
print(f"Your name is {name}, your fav game is {fav_game}, your balance is £{money:.2f}.")

#PART 3
no_of_games = int(input("How many games you wanna play"))
games_cost = 2.50
total_cost = games_cost * no_of_games
remaining = money - total_cost
if(remaining < 0):
    print("watch out bro")
else:
    print(f"there is £{remaining:.2f} of ur moneys left")


#Part 4
scores = []
scores.append(int(input("games score 1:")))
scores.append(int(input("games score 2:")))
scores.append(int(input("games score 3:")))
print(scores)
print(max(scores))
print(min(scores))
average = sum(scores) / len(scores)
print(average)
scores.append(50)
scores.remove(min(scores))
print(scores)
