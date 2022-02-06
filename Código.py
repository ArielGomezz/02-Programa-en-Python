print("")
print ("-----------------------------BIENVENIDOS---------------------------------")
print("")

area = str
sueldo = float
promedio = float
final = float
totalEmpleadosArmado = 0
totalEmpleadosEmpaquetado  = 0
totalEmpleadosVentas = 0
promedio = 0
final = 0

while area != "fin":

    area = input("INGRESAR AREA: (A- armado, E- empaquetado, V- ventas) FIN para finalizar : ")
    if area != "fin":
        sueldo =float(input("Ingresar Sueldo : $ "))
    
    
    if area == "a" or area == "A":
        totalEmpleadosArmado = totalEmpleadosArmado + 1

    elif area =="e" or area == "E":
        totalEmpleadosEmpaquetado = totalEmpleadosEmpaquetado + 1

    elif area == "v" or area == "V":
        totalEmpleadosVentas =  totalEmpleadosVentas + 1

        
    promedio = (promedio + sueldo)


totalGeneral = totalEmpleadosArmado + totalEmpleadosEmpaquetado + totalEmpleadosVentas

final = (promedio / totalGeneral)


print("")
print("---------------------------------------------------------------------------")
print ("Total Empleado del Area Armado : ", totalEmpleadosArmado)
print("---------------------------------------------------------------------------")
print ("Total Empleados del Area Empaquetado: ", totalEmpleadosEmpaquetado)
print("---------------------------------------------------------------------------")
print("Total Empleados del Area Ventas: ",  totalEmpleadosVentas)
print("---------------------------------------------------------------------------")
print("Total General de Empleados : ", totalGeneral)
print("---------------------------------------------------------------------------")
print("Sueldo Promedio : $ ", final)


    
    


