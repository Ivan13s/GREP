import random

c = 0
while c< 3:
    alegere_fruct = input("Alege un fruct:")
    lista_goala = []
    lista_goala.append(alegere_fruct)
    print(lista_goala)
    c=c+1
    break

while True:
    ani = random.randint(20, 25)
    print("Anii random:", ani)
    if ani == 23:
        print("Izabell are 23 de ani,deci este bombardiera")
        break
    else:
        print("Izabell nu este bombardiera deci nu are 23 de ani")
