few = int(input())
lot = int(input())
sleep = int(input())

if sleep < few:
    print('Недосып')
elif sleep > lot:
    print('Пересып')
else:
    print('Это нормально')