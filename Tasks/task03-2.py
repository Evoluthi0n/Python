num1 = input("Введите первое дробное число: ").split(".")
num2 = input("Введите второе дробное число: ").split(".")
sum1 = int(num1[0])+int(num2[0])
sum2 = float("0."+num1[1])+float("0."+num2[1])
print("Сумма целых частей: ",sum1,"\nСумма дробных частей: ",sum2)