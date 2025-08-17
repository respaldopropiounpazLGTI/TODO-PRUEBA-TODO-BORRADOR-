#encoding:UTF-8
'''
Salario bruto de 100.000 ARS, los descuentos típicos serían los siguientes:
Aportes Jubilatorios (11%):	100.000 ARS × 11% = 11.000 ARS
Obra Social (3%):100.000 ARS × 3% = 3.000 ARS
Total de Descuentos:
		11.000 ARS (Aportes Jubilatorios)
		3.000 ARS (Obra Social)
Total de Descuentos: 11.000 + 3.000  = 14.000 ARS
Sueldo Neto: 100.000 ARS - 14.000 ARS = 86.000 ARS
'''

visueldobruto= int(input("Ingrese el valor de sueldo bruto: "))
otrosDescuento= int(input("Ingrese el valor de otros descuentos: "))
porcentajeaportesjubilatorios= 11
porcentajeobrasocial= 3
totalpordescuentos=porcentajeobrasocial+porcentajeaportesjubilatorios+otrosDescuento
montodescuento = visueldobruto * totalpordescuentos/100
sueldoNeto= visueldobruto - montodescuento
print("******************************************************")
print(f"El monto de descuento es:",montodescuento)
print("El sueldo neto es:", int(sueldoNeto))
print("El porcentaje de descuento es: ", totalpordescuentos, "%")
print("******************************************************")