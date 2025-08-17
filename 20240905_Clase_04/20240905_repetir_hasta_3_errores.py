vi_cont_posit = 0
vi_error = 0
ci_VIDAS= 3
while True:
    numero=int(input("Ingrese un numero: "))
    if numero>0:
        vi_cont_posit=vi_cont_posit+1
    else:
        vi_error+=1
        print(f"Error {vi_error} / {ci_VIDAS}")
    if vi_error==ci_VIDAS:
        break

print(f"La cantidad de numeros positivos es: {vi_cont_posit}")