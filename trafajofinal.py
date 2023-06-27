import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data.csv",sep=',',encoding="utf-8") #lee el documento
print(data)
print(data.head())
def mostrar_casos_por_anio():
    #filtrar datos
    data_filtered = data[(data['Año de los casos'] >= 2017) & (data['Año de los casos'] <= 2022)]
    #Porcentajes de Año
    casos_por_anio = data_filtered['Año de los casos'].value_counts().sort_index()
    porcentajes = casos_por_anio / casos_por_anio.sum() *  100
    porcentajes = porcentajes.reset_index()

    plt.xlabel('Año')
    plt.ylabel('Cantidad de casos')
    plt.title('Cantidad de casos de violencia sexual por Año') #título del grafico
    #Grafico por Año
    casos_por_anio.plot(kind='bar',figsize=(8,6))
    for i, v in enumerate(casos_por_anio):
        print('i ', i)
        print('v ', v)
        plt.text(i, v + 1, f'{porcentajes["count"][i]:.2f}%', ha='center', color='black')
    # plt.figure(figsize=(8,6)) #tamanio de la figura
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
    casos_por_edad = data['Rango de edad de la victima'].value_counts().sort_index()
    casos_por_edad.plot(kind='bar',figsize=(12,6))
    plt.xlabel('Edad')
    plt.ylabel('Cantidad por las edades')
    plt.title('Cantidad de casos de violencia sexual por edades')
    plt.show()

#Menu
while True:
    print("- - - - -Menu- - - - -")
    print("1. Mostrar casos por año")
    print("2. Mostrar casos por mes")
    print("3. Mostrar casos por departamento")
    print("4. Mostrar casos por edades")
    print("0. Exit")
    opcion =input("Ingrese una opcion: ")
    if opcion == "1":
        mostrar_casos_por_anio()
    elif opcion == "2":
        mostrar_casos_por_mes()
    elif opcion == "3":
        mostrar_casos_por_departamento()
    elif opcion == "4":
        mostrar_casos_por_edades()
    elif opcion == "0":
        break
    else:
        print("Opcion incorrecta. Ingrese nuevamente una opcion")
