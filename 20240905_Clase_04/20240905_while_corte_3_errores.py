vi_cont_posit = 0
vi_error = 0
ci_VIDAS= 3
while vi_error!=ci_VIDAS:
    numero=int(input("Ingrese un numero: "))
    if numero>0:
        vi_cont_posit=vi_cont_posit+1
    else:
        vi_error+=1
        print(f"Error {vi_error} / {ci_VIDAS}")

print(f"La cantidad de numeros positivos es: {vi_cont_posit}")