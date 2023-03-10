

print("keys".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7, 'country': 'Argentina'}

print(f"player :{player}")

print("-" * 40)

k = player.keys()       # extracts all the keys from the dictionary
print(k)

for k in player.keys():
    print(k, "=>", player[k])

print("values".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7, 'country': 'Argentina'}

print(f"player :{player}")

v = player.values()
print(v)

print("items".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7, 'country': 'Argentina'}

print(f"player :{player}")

print("-" * 40)

for k, v in player.items():
    print(k,"\t=>\t", v)

print("get".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7}

print(f"player :{player}")
print("-" * 40)

print(f"Name :{player.get('name', 'Please enter a valid key')}")
print(f"Country :{player.get('country', 'Please enter a valid key')}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("setdefault".center(40, "-"))

player = {'name': 'Lionel Messi', 'age': 35, 'goals': 380, 'club': 'PSG', 'ballondors': 7}

print(f"player :{player}")

player.setdefault('name', 'Messi')
player.setdefault('club', 'FCB')
player.setdefault('country', "Argentina")

print(f"player :{player}")
