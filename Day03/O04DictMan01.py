
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Mark'), ('age', 32), ('dept', 'finance'), ('desig', 'MGR'), ('sal', 85000)])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='Messi', age=35, goals=350, club='psg', ballondors=7)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = dict(name='Messi', age=35, goals=350, club='PSG', ballondors=7)
print(f"player :{player}")

print("-" * 40)
# read
print(f"Name :{player['name']}")
print(f"Club :{player['club']}")

print("-" * 40)
for x in player:
    print(x + " => " + str(player[x]))

# modify
print("-" * 40)
player['name'] = "Lionel Messi"
player['goals'] = 380
player['country'] = 'Argentina'

print(f"player :{player}")

print("-" * 40)
# del
del player['age']
del player['club']

print(f"player :{player}")

print("-" * 40)
print(dir(player))



