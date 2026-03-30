from math import sqrt

def EucledianD(p1, p2):
    return sqrt(((p1['X'] - p2['X']) ** 2) + ((p1['Y'] - p2['Y']) ** 2))

data = [
    {'X' : 1, 'Y' : 2, 'Label' : 'Red'},
    {'X' : 2, 'Y' : 3, 'Label' : 'Red'},
    {'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
    {'X' : 6, 'Y' : 5, 'Label' : 'Blue'}
]

user_point = {}

x1 = int(input("Enter x coordinate : "))
y1 = int(input("Enter Y coordinate : "))

user_point['X'] = x1
user_point['Y'] = y1

for d in data:
    d['distances'] = EucledianD(d, user_point)
    

sorted_data = sorted(data, key=lambda x: x['distances'])

for d in sorted_data:
    print(d)