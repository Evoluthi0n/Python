a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f'1) {a} + {b}', f"2) {a} - {b}", f"3) {a} * {b}",f"4) {a} / {b}",f"5) {a} % {b}",sep = "\n")
act = int(input("Выберите действие [1-5]:"))
print("Результат операции")
if act ==1:
    print(str(a+b))
elif act ==2:
    print(str(a-b))
elif act ==3:
    print(str(a*b))
elif act ==4 or act ==5:
    if b==0:
        print("Нельзя делить на 0")
    elif act == 4:    
        print(str(a/b))
    elif act ==5:
        print(str(a % b))