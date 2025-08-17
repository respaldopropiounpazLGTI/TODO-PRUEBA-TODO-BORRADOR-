print(range(1,6))
#range(1, 6)
#[1, 2, 3, 4, 5]
print(list(range(1,20)))
for i in range(1,20,1):
    if i%2!=0:
        print("es impar el:",i)
    else:
        print(f"es par el:{i}")

for i in range(1,20,2):
    print("ABAJO es impar el:",i)

for i in range(0,20,2):
    print("MAS ABAJO es par el:",i)

#Comparamos como se arma una lista incremetal y decremental
print(list(range(20,0,-1)))
print(list(range(0,20,1)))
for i in range(20,0,-1):
    print("pa'tras el for el:",i)