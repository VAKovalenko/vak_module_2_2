first = int(input('Введите первую переменную: '))
second = int(input('Введите вторую переменную: '))
third = int(input('Введите третью1 переменную: '))

if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
