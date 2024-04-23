mass = input("Введите массу: ").split(".")
print("Масса: " + mass[0] + " тонн, " + str(int(mass[1])//1000) + " килограмм, " + str(int(mass[1])-(int(mass[1])//1000)*1000) + " грамм")