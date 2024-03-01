"""
Empresas Camisuchis
Ejercicio No.1
Caculo de salario neto de empleado
"""

print("Bienvenido a Empresas Camisuchis")
salario_bruto = int(input("Ingrese el salario bruto del empleado: "))
camisas_vendidas = int(input("Ingrese la cantidad de camisas vendidas: "))

cantidad_empleados = 10

for empleado in range(cantidad_empleados):
    if salario_bruto > 1000000:
        seguro_salud = salario_bruto * 0.08
        impuesto_renta = salario_bruto * 0.12
        costo_camisa = 15000
        regalias = (costo_camisa * camisas_vendidas) * 0.03
    else:
        seguro_salud = salario_bruto * 0.08
        impuesto_renta = salario_bruto * 0.12
        costo_camisa = 15000
        regalias = (costo_camisa * camisas_vendidas) * 0.03


    salario_neto = salario_bruto - seguro_salud - impuesto_renta + regalias
    print(f"Salario total del empleado a  final de mes es: {salario_neto}")