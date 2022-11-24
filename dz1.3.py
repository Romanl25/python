print('Введите координаты точки')

x = int(input('x= '))

y = int(input('y= '))

if x>0:
   if y>0:
       print('Точка лежит в 1 четверти')
   else:
       print('Точка лежит в 2 четверти')
else:
   if y>0:
       print('Точка лежит в 3 четверти')
   else:
       print('Точка лежит в 4 четверти')