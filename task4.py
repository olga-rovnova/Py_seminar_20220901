# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

ch=int(input('введите номер четверти: '))
if ch==1:
    print('x>0\ny>0')
elif ch==2:
    print('x<0\ny>0')  
elif ch==3:
    print('x<0\ny<0')  
else:
    print('x>0\ny>0')