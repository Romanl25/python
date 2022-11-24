import random

x = random.randint(-100, 100) 
print('x =', x)

y = random.randint(-100, 100) 

print('y =', y)

if x > 0 and y > 0:

    print ("Точка находится в 1 четверти")

elif x < 0 and y > 0:

    print ("Точка находится в 2 четверти")

elif x < 0 and y < 0:

    print ("Точка находится в 3 четверти")

elif x > 0 and y < 0:

    print("Точка находится в 4 четверти")