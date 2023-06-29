from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("data1.csv",sep=',',encoding="utf-8") #lee el documento
# print(data)
# print(data.head())
def mostrar_casos_por_anio():
    #filtrar datos
    data_filtered = data[(data['Año'] >= 2017) & (data['Año'] <= 2022)]
    #Porcentajes de Año
    casos_por_anio = data_filtered['Año'].value_counts().sort_index()
    porcentajes = casos_por_anio / casos_por_anio.sum() *  100
    #Grafico por Año
    casos_por_anio.plot(kind='bar',figsize=(8,6))
    for i, v in enumerate(casos_por_anio):
        plt.text(i, v + 1, f'{porcentajes[i]:.2f}%', ha='center', color='black') #texto a el gráfico
    plt.figure(figsize=(8,6)) #tamanio de la figura
    plt.xlabel('Año')
    plt.ylabel('Cantidad de casos')
    plt.title('Cantidad de casos de violencia sexual por Año') #título del grafico
    plt.show()

def mostrar_casos_por_mes():
    #Porcentaje por mes
    casos_por_mes = data['Mes'].value_counts().sort_index()
    porcentajes = casos_por_mes / casos_por_mes.sum() * 100
    #Grafico por Mes
    casos_por_mes.plot(kind='bar',figsize=(8,6))
    for i, v in enumerate(casos_por_mes):
        plt.text(i, v + 1, f'{porcentajes[i]:.2f}%', ha='center', color='black')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de casos')
    plt.title('Cantidad de casos de violencia sexual por Mes')
    plt.show()

def mostrar_casos_por_departamento():
    #Porcentaje por Provincia
    casos_por_provincia = data['Departamento'].value_counts()
    porcentajes = casos_por_provincia / casos_por_provincia.sum() * 100
    #Grafico por Provincia
    casos_por_provincia.plot(kind='bar',figsize=(12,6))
    for i, v in enumerate(casos_por_provincia):
        plt.text(i, v + 1, f'{porcentajes[i]:.2f}%', ha='center', color='black') 
    plt.xlabel('Provincia')
    plt.ylabel('Cantidad de casos')
    plt.title('Cantidad de casos de violencia sexual por Provincia')
    plt.show() 

def mostrar_casos_por_edades():
    #Grafico barras por edades
    # casos_por_edad = data['Rango de edad de la victima'].value_counts().sort_index()
    casos_por_edad = data['Rango de edad de la víctima'].value_counts().sort_index()
    casos_por_edad.plot(kind='bar',figsize=(12,6))
    plt.xlabel('Edad')
    plt.ylabel('Cantidad por las edades')
    plt.title('Cantidad de casos de violencia sexual por edades')
    plt.show()

def mostrar_departamentos_por_anio():
    año = input("Ingrese el año: ")
    data_filtered = data[data['Año de los casos'] == int(año)]
    casos_por_departamento = data_filtered['Departamento'].value_counts()

    plt.title(f'Departamentos con casos de violencia sexual en el año {año}')
    casos_por_departamento.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend(casos_por_departamento.index, loc='best')
    plt.show()

def mostrar_casos_por_tipo_violencia():
    año = input("Ingrese el año: ")
    mes = str(input("Ingrese el mes: "))
    departamento = str(input("Ingrese el departamento: "))

    data_filtered = data[(data['Año de los casos'] == int(año)) & (data['Mes'] == int(mes)) & (data['Departamento'] == departamento)]
    casos_por_tipo_violencia = data_filtered['Tipo de violencia'].value_counts()

    plt.title(f'Casos de violencia sexual por tipo en {mes}/{año}, {departamento}')
    casos_por_tipo_violencia.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend(casos_por_tipo_violencia.index, loc='best')
    plt.show()
    
def mostrar_casos_por_etnica():
    año = input("Ingrese el año: ")
    mes = str(input("Ingrese el mes: "))
    departamento = str(input("Ingrese el departamento: "))
    data_filtered = data[(data['Año de los casos'] == int(año)) & (data['Mes'] == int(mes)) & (data['Departamento'] == departamento)]
    casos_por_etnica = data_filtered['Casos por etnica'].value_counts()

    plt.title(f'Casos de violencia sexual por autoidentificación étnica en {mes}/{año}, {departamento}')
    casos_por_etnica.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend(casos_por_etnica.index, loc='best')
    plt.show()

def mostrar_por_accionesPreventivas():
    año = input("Ingrese el año: ")
    mes = input("Ingrese el mes: ")
    departamento = input("Ingrese el departamento: ")

    data_filtered = data[(data['Año de los casos'] == int(año)) & (data['Mes'] == int(mes)) & (data['Departamento'] == departamento)]
    acciones_preventivas = data_filtered['Acciones preventivas'].value_counts()

    plt.title(f'Acciones preventivas en casos de violencia sexual en {mes}/{año}, {departamento}')
    acciones_preventivas.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend(acciones_preventivas.index, loc='best')
    plt.show()

def mostrar_por_centras_masUtilizados():
    año = input("Ingrese el año: ")
    mes = input("Ingrese el mes: ")
    departamento = input("Ingrese el departamento: ")

    data_filtered = data[(data['Año de los casos'] == int(año)) & (data['Mes'] == int(mes)) & (data['Departamento'] == departamento)]
    centros_mas_utilizados = data_filtered['Centros más utilizados'].value_counts()

    plt.title(f'Centros más utilizados en casos de violencia sexual en {mes}/{año}, {departamento}')
    centros_mas_utilizados.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend(centros_mas_utilizados.index, loc='best')
    plt.show()


#Menu
def mostrar_estadisticas():
    while True:
        print("\n--- Estadísticas ---")
        print("1. Mostrar casos por año")
        print("2. Mostrar casos por mes")
        print("3. Mostrar casos por departamento")
        print("4. Mostrar casos por edades")
        print("5. Mostrar casos de departamentos por año")
        print("6. Mostrar casos por tipo de violencia")
        print("7. Mostrar casos por autoidentificación étnica")
        print("8. Mostrar por acciones preventivas")
        print("9. Mostrar por centros más utilizados")
        print("0. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_casos_por_anio()
        elif opcion == "2":
            mostrar_casos_por_mes()
        elif opcion == "3":
            mostrar_casos_por_departamento()
        elif opcion == "4":
            mostrar_casos_por_edades()
        elif opcion == "5":
            mostrar_departamentos_por_anio()
        elif opcion == "6":
            mostrar_Casos_por_violencia()
        elif opcion == "7":
            mostrar_casos_por_etnica()
        elif opcion == "8":
            mostrar_por_accionesPreventivas()
        elif opcion == "9":
            mostrar_por_centras_masUtilizados()
        elif opcion == "0":
            break
        else:
            print("Opción incorrecta. Ingrese nuevamente una opción.")

from tabulate import tabulate

def mostrar_todos_los_datos_ordenados():
        print("Primeros 5 datos:")
        primeros_5 = data.head(5)
        print(tabulate(primeros_5, headers='keys', tablefmt='grid'))
    
        print("\nÚltimos 5 datos:")
        ultimos_5 = data.tail(5)
        print(tabulate(ultimos_5, headers='keys', tablefmt='grid'))

def cerrar_programa():
    print("Cerrando el programa...")
    

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Instrucciones del menú")
        print("2. Mostrar estadísticas")
        print("3. Mostrar los datos ordenados")
        print("4. Cerrar el programa")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Instrucciones del menú
            print("¡Bienvenido al programa de estadísticas!")
            print("Este programa te permite acceder a diferentes estadísticas sobre casos de violencia sexual.")
            print("Por favor, selecciona la opción deseada del menú.")
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            mostrar_todos_los_datos_ordenados()
        elif opcion == "4":
            cerrar_programa()
            break
        else:
            print("Opción incorrecta. Ingrese nuevamente una opción.")

menu_principal()