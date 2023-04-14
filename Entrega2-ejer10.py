import string
from collections import Counter
#importo las librerias que me pueden llegar a ser utiles
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#Instancio una variable de tipo diccionario para ir uniendo según el alumno, las notas
alumnos = {}

# SECCION DE FUNCIONES: COMIENZO

def enlazarAlumnoNota(nom, puntaje1, puntaje2, dic):
  """funcion que agrega al diccionario de alumnos, el nombre como clave, y las notas como diccionario dentro del alumno para tener 2 valores organizados"""
  dic[nom] = {"nota1": puntaje1, "nota2": puntaje2}

#------------------------------------------------------------------------------------------------------------

def corroborarAlumno(dic):
  """FUNCIÓN QUE SOLICITA UN ALUMNO E IMPRIME LA/S NOTA/S CORRESPONDIENTES"""
  alumno_ingresado = input("ingrese un alumno(fin para finalizar): ")
  while (alumno_ingresado != "fin"):
    alumno_ingresado = alumno_ingresado.lower()
    cant_notas = input("Ingrese 'T' para ver todas las notas/Ingrese nota1 para ver la nota 1/Ingrese nota2 para ver la nota 2: ")
    cant_notas = cant_notas.lower().replace(" ","")
    match cant_notas:
      case "t":
        print(f"el alumno {alumno_ingresado} tiene {alumnos[alumno_ingresado]}")
      case "nota1":
        print(f"el alumno {alumno_ingresado} tiene en nota 1: {alumnos[alumno_ingresado]['nota1']}")
      case "nota2":
        print(f"el alumno {alumno_ingresado} tiene en nota 2: {alumnos[alumno_ingresado]['nota2']}")
    alumno_ingresado = input("ingrese un alumno(fin para finalizar): ")

#------------------------------------------------------------------------------------------------------------

def promedioAlumno(n1,n2,nom):
  """CALCULA PROMEDIO DE ALUMNO"""
  suma = n1 + n2
  promedio = suma/2
  print(f"el promedio del alumno {nom} es: {promedio}")

#------------------------------------------------------------------------------------------------------------

def sumarnotas(n1,n2):
  """SUMA 2 NOTAS DEL ALUMNO Y RETORNA EL TOTAL SUMADO"""
  sum = n1 + n2
  return sum

#------------------------------------------------------------------------------------------------------------

def promedioDelCurso(alumn): #el promedio del curso lo voy a calcular en base a esta definicion:El promedio general (GPA) se obtiene dividiendo el número total de calificaciones obtenidas por la cantidad total de horas cursadas.
  """CALCULA EL PROMEDIO GENERAL DEL CURSO"""
  total = 0
  for nom,valor in alumn.items():
    total = total + sumarnotas(valor['nota1'],valor['nota2'])
  print(f"promedio general del curso: {total/200}") #voy a asumir que el curso duró 200 horas, a modo de ejemplo. No entiendo bien a qué hace referencia el promedio general del curso, por lo que me baso en esa definicion

#------------------------------------------------------------------------------------------------------------

def promedioDeCadaAlumno(alu):
  """FUNCIÓN QUE CALCULA EL PROMEDIO DE CADA ALUMNO Y LO IMPRIME EN BASE A UN DICCIONARIO"""
  for nom, valor in alu.items():
    promedioAlumno(valor['nota1'],valor['nota2'], nom)
  
#------------------------------------------------------------------------------------------------------------

def calcularMax(nombre,prom,maximoprom,maxnombre):
  """FUNCION QUE COMPARA EL PROMEDIO CON EL MAS ALTO QUE SE TIENE GUARDADO, Y SI ES MAYOR EL ACTUAL, SE ACTUALIZA EL MAXIMOPROM Y MAXNOMBRE"""
  if (prom > maximoprom):
    maxnombre = nombre
    maximoprom = prom
  return maxnombre,maximoprom


#------------------------------------------------------------------------------------------------------------

def calcularMin(nom,prom,min_n,min_pr):
  """FUNCION QUE COMPARA EL PROMEDIO MINIMO CON EL PROMEDIO ACTUAL Y SI ES MENOR LO REEMPLAZA"""
  if (prom<min_pr):
    min_n = nom
    min_pr = prom
  return min_n, min_pr

#------------------------------------------------------------------------------------------------------------

def promedioMinimoAlumno(alum):
  minprom = 9999
  min_nombre = "zzz"
  for nom,valor in alum.items():
    x = sumarnotas(valor['nota1'],valor['nota2'])/2
    min_nombre, minprom = calcularMin(nom,x,min_nombre,minprom)
  return min_nombre,minprom

#------------------------------------------------------------------------------------------------------------

def maximoPromedioAlumno(alum):
  """FUNCION QUE CALCULA CUAL ES EL PROMEDIO MAS ALTO EN EL DICCIONARIO DE ALUMNOS E IMPRIME EL RESULTADO"""
  max_actual = -1
  nombre_max = "zzz"
  for nombre,valor in alum.items():
    x = sumarnotas(valor['nota1'],valor['nota2'])/2
    nombre_max, max_actual = calcularMax(nombre,x,max_actual,nombre_max)
  return nombre_max, max_actual

#------------------------------------------------------------------------------------------------------------



#SECCIÓN DE FUNCIONES: FINAL

nombres2 = nombres.lower().replace(",","").replace("'"," ").split()
contador = len(nombres2)  #Inicia el for, el cual se repite la misma cantidad que alumnos haya.

for iterador in range(0,contador):
  enlazarAlumnoNota(nombres2[iterador], notas_1[iterador], notas_2[iterador], alumnos)
#finaliza el for


corroborarAlumno(alumnos) #no es para ningun item en especial, solo para comprobar que se enlazó bien los nombres y notas.

print("-"*50)
#ITEM B
print("se imprime a continuación el promedio de cada alummno----")
promedioDeCadaAlumno(alumnos)

print("-"*50)
#ITEM C
print("se imprime a continuación el promedio general del curso----")
promedioDelCurso(alumnos)

print("-"*50)
#ITEM D
print("Se imprime a continuación el alumno con el promedio mas alto de todos")
maxnombfinal,maxpromedio = maximoPromedioAlumno(alumnos)
print(f"{maxnombfinal} tiene la nota promedio mas alta con un puntaje de {maxpromedio}")

print("-"*50)
#ITEM E // EN LA PRACTICA DEL JUEVES NOS DIJERON QUE EN REALIDAD ESTE ITEM SE REFIERE AL PROMEDIO MAS BAJO Y NO A LA NOTA MAS BAJA, POR LO QUE CALCULO EL PROMEDIO MAS BAJO
print("Se imprime a continuación el alumno con el promedio más bajo de todos")
minnombfinal,minpromedio = promedioMinimoAlumno(alumnos)
print(f"{minnombfinal} tiene la nota promedio mas baja con un puntaje de {minpromedio}")
