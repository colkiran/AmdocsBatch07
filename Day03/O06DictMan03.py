
print("pop".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7, 'country': 'Argentina'}

print(f"player :{player}")

res1 = player.pop('age')
print(f"res1 :{res1}")

res2 = player.pop('club')
print(f"res2 :{res2}")

# res2 = player.pop()
# print(f"res2 :{res2}")

print(f"player:{player}")

print("popitem".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7, 'country': 'Argentina'}

print(f"player :{player}")

res1 = player.popitem()
print(f"res1 :{res1}")

res2 = player.popitem()
print(f"res2 :{res2}")

print(f"player :{player}")

print("clear".center(40, "-"))
player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG'}
print(f"player :{player}")

player.clear()
print(f"player :{player}")

print("update".center(40, "-"))
player1 = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'country':'Argentina'}

player2 = {'name': 'Cristiano Ronaldo', 'age': 37, 'goals': 360, 'club': 'AL Nassr FC', 'ballondors': 4}

print(f"player1 :{player1}")
print(f"player2 :{player2}")

print("-" * 40)

player1.update(player2)
print(f"player1 :{player1}")
print(f"player2 :{player2}")

