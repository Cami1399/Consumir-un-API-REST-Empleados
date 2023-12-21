import requests

# Hacer la solicitud GET a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
datos = requests.get(url).json()['data']
#print (datos)

# Obtener la cantidad de empleados
num_empleados = len(datos)

# Calcular el promedio de salario de los empleados
salarios = [empleado['employee_salary'] for empleado in datos]
promedio_salario = sum(salarios) / len(salarios)

# Calcular el promedio de edad de los empleados
edades = [empleado['employee_age'] for empleado in datos]
promedio_edad = sum(edades) / len(edades)

# Encontrar salario mínimo y máximo
salario_min = min(salarios)
salario_max = max(salarios)

# Encontrar la edad menor y mayor de los empleados
edad_min = min(edades)
edad_max = max(edades)

# Mostrar los resultados
print(f"Cantidad de empleados: {num_empleados}")
print(f"Promedio de salario: {promedio_salario}")
print(f"Promedio de edad: {promedio_edad}")
print(f"Salario mínimo: {salario_min}")
print(f"Salario máximo: {salario_max}")
print(f"Edad menor: {edad_min}")
print(f"Edad mayor: {edad_max}")
