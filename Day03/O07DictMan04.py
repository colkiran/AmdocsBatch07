


emp1 = {'name': 'Ben', 'age': 32, 'exp': '8 yrs'}
print(f"emp1 before :{emp1}")

emp2 = emp1         # shallow copy

print(f"emp2 before  :{emp2}")

print("-" * 40)
emp2['dept'] = "MKT"
emp2['loc'] = 'HYD'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("\n", "-" * 40, "\n")
emp3 = {'name': 'Kevin', 'age': 29, 'dept': 'Fin'}
print(f"emp3 before  :{emp3}")

emp4 = emp3.copy()              # deep copy
print(f"emp4 before :{emp4}")
print("-" * 40)

emp4['sal'] = 35000
emp4['loc'] = 'Bangalore'
print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("\n", "-" * 40, "\n")
emp5 = {'name': 'Ben', 'age': 32, 'exp': {'hp': '5 yrs', 'ibm': '3 yrs'}}
print(f'emp5 before :{emp5}')

emp6 = emp5.copy()
print(f"emp6 before :{emp6}")
print("-" * 40)

emp6['exp']['dell'] = '2 yrs'
emp6['exp']['Ness'] = '1 yrs'

print(f"emp6 after :{emp6}")
print(f'emp5 after :{emp5}')

print("\n", "-" * 40, "\n")
emp7 = {'name': 'Ben', 'age': 32, 'exp': {'hp': '5 yrs', 'ibm': '3 yrs'}}
print(f'emp7 before :{emp7}')

from copy import deepcopy
emp8 = deepcopy(emp7)
print(f"emp8 before :{emp8}")

print("-" * 40)

emp8['exp']['dell'] = '2 yrs'
emp8['exp']['Ness'] = '1 yrs'

print(f"emp8 after :{emp8}")
print(f'emp7 after :{emp7}')
