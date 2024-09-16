numb1 = int(input("Inicio del rango"))
numb2 = int(input("Fin del rango"))
for i in range(numb1, numb2+1):
    if i % 2 == 0:
        print(i)