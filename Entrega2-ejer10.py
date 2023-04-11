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
def enlazarAlumnoNota(nom, puntaje1, puntaje2, dic):
  """funcion que agrega al diccionario de alumnos, el nombre como clave, y las notas como diccionario dentro del alumno para tener 2 valores organizados"""
  dic[nom] = {"nota1": puntaje1,"nota2": puntaje2}
#FIN

nombres2 = nombres.lower().replace(",","").replace("'"," ").split()

contador = len(nombres2)  #Inicia el for, el cual se repite la misma cantidad que alumnos haya.
print(contador)
for iterador in range(0,contador):
  auxnom = nombres2[iterador]
  auxn1 = notas_1[iterador]
  auxn2 = notas_2[iterador]
  enlazarAlumnoNota(nombres2[iterador], notas_1[iterador], notas_2[iterador], alumnos)
#finaliza el for


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
