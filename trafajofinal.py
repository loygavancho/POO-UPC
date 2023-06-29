import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("data1.csv",sep=',',encoding="utf-8") #lee el documento
# print(data)
# print(data.head())
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
    # casos_por_edad = data['Rango de edad de la victima'].value_counts().sort_index()
    casos_por_edad = data['Rango de edad de la víctima'].value_counts().sort_index()
    casos_por_edad.plot(kind='bar',figsize=(12,6))
    plt.xlabel('Edad')
    plt.ylabel('Cantidad por las edades')
    plt.title('Cantidad de casos de violencia sexual por edades')
    plt.show()

def mostrar_departamentos_por_anio():
    departamentos = {
        1: "Lima",
        2: "Madre de Dios",
        3: "Piura",
        4: "La Libertad",
        5: "Ayacucho",
        6: "San Martín",
        7: "Huánuco",
        8: "Puno",
        9: "Tacna",
        10: "Loreto",
        11: "Ucayali",
        12: "Tumbes",
        13: "Lambayeque",
        14: "Amazonas",
        15: "Ica",
        16: "Moquegua",
        17: "Junín",
        18: "Cusco",
        19: "Cajamarca",
        20: "Áncash",
        21: "Pasco",
        22: "Huancavelica",
        23: "Arequipa",
        24: "Apurímac",
        25: "Callao"
    }
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
    año = input("Ingrese el año: ")
    if int(año) < 2017 or int(año) > 2023:
        print("Año inválido. Ingrese un año válido de cuatro dígitos.")
        return
    
    mes = input("Ingrese el mes (1-12): ")
    if int(mes) not in range(1, 13):
        print("Mes inválido. Ingrese un número de mes válido (1-12).")
        return
    departamento = input("Ingrese el departamento (1-25): ")           
    if int(departamento) in range(1, 26):
        print("Departamento inválido. Ingrese un número de departamento válido (1-25).")
        return
    departamento_label = departamentos.get(int(departamento), "Desconocido")
    mes_label = meses.get(int(mes), "Desconocido")
    
    data_filtered = data[
        (data['Año de los casos'] == int(año)) &
        (data['Mes'] == int(mes)) &
        (data['Departamento'] == departamento_label)
    ]
    casos_por_departamento = data_filtered[data_filtered['Departamento'] == departamento_label]
    casos_por_departamento = casos_por_departamento['Departamento'].value_counts()
    plt.title(f'Departamentos con casos de violencia sexual en el mes {mes_label}')
    casos_por_departamento.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend([departamento_label], loc='best')
    plt.show()
             

def mostrar_casos_por_etnica():
    departamentos = {
        1: "Lima",
        2: "Madre de Dios",
        3: "Piura",
        4: "La Libertad",
        5: "Ayacucho",
        6: "San Martín",
        7: "Huánuco",
        8: "Puno",
        9: "Tacna",
        10: "Loreto",
        11: "Ucayali",
        12: "Tumbes",
        13: "Lambayeque",
        14: "Amazonas",
        15: "Ica",
        16: "Moquegua",
        17: "Junín",
        18: "Cusco",
        19: "Cajamarca",
        20: "Áncash",
        21: "Pasco",
        22: "Huancavelica",
        23: "Arequipa",
        24: "Apurímac",
        25: "Callao"
    }
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
    año = input("Ingrese el año: ")
    if int(año) < 2017 or int(año) > 2023:
        print("Año inválido. Ingrese un año válido de cuatro dígitos.")
        return
    
    mes = input("Ingrese el mes (1-12): ")
    if int(mes) not in range(1, 13):
        print("Mes inválido. Ingrese un número de mes válido (1-12).")
        return
    departamento = input("Ingrese el departamento (1-25): ")           
    if int(departamento) in range(1, 26):
        print("Departamento inválido. Ingrese un número de departamento válido (1-25).")
        return

    departamento_label = departamentos.get(int(departamento), "Desconocido")
    mes_label = meses.get(int(mes), "Desconocido")
    
    data_filtered = data[
        (data['Año de los casos'] == int(año)) &
        (data['Mes'] == int(mes)) &
        (data['Departamento'] == departamento_label)
    ]
    casos_por_autoidentificacion = data_filtered['Autoidentificadores étnicos'].value_counts()
    plt.title(f'Casos de violencia sexual por autodentificacion etnica en {mes_label}/{año}, {departamento_label}')
    casos_por_autoidentificacion.plot(kind='pie', figsize=(8,6), autopct='%1.1f%%')
    plt.ylabel('')
    plt.legend(casos_por_autoidentificacion.index, loc='best') 
    plt.show()

def mostrar_por_accionesPreventivas():
   departamentos = {
        1: "Lima",
        2: "Madre de Dios",
        3: "Piura",
        4: "La Libertad",
        5: "Ayacucho",
        6: "San Martín",
        7: "Huánuco",
        8: "Puno",
        9: "Tacna",
        10: "Loreto",
        11: "Ucayali",
        12: "Tumbes",
        13: "Lambayeque",
        14: "Amazonas",
        15: "Ica",
        16: "Moquegua",
        17: "Junín",
        18: "Cusco",
        19: "Cajamarca",
        20: "Áncash",
        21: "Pasco",
        22: "Huancavelica",
        23: "Arequipa",
        24: "Apurímac",
        25: "Callao"
   }
   meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
   }
   año = input("Ingrese el año: ")
   if int(año) < 2017 or int(año) > 2023:
        print("Año inválido. Ingrese un año válido de cuatro dígitos.")
        return
    
   mes = input("Ingrese el mes (1-12): ")
   if int(mes) not in range(1, 13):
        print("Mes inválido. Ingrese un número de mes válido (1-12).")
        return
   departamento = input("Ingrese el departamento (1-25): ")           
   if int(departamento) in range(1, 26):
        print("Departamento inválido. Ingrese un número de departamento válido (1-25).")
        return

   departamento_label = departamentos.get(int(departamento), "Desconocido")
   mes_label = meses.get(int(mes), "Desconocido")
    
   data_filtered = data[
        (data['Año de los casos'] == int(año)) &
        (data['Mes'] == int(mes)) &
        (data['Departamento'] == departamento_label)
   ]
   acciones_preventivas = data_filtered['Acciones preventivas'].value_counts()
   plt.title(f'Acciones preventivas en casos de violencia sexual en {mes_label}/{año}, {departamento_label}')
   acciones_preventivas.plot(kind='pie', figsize=(8,6), autopct='%1.1f%%')
   plt.ylabel('')
   plt.legend(acciones_preventivas.index, loc='best') 
   plt.show()

def mostrar_por_centras_masUtilizados():
    departamentos = {
        1: "Lima",
        2: "Madre de Dios",
        3: "Piura",
        4: "La Libertad",
        5: "Ayacucho",
        6: "San Martín",
        7: "Huánuco",
        8: "Puno",
        9: "Tacna",
        10: "Loreto",
        11: "Ucayali",
        12: "Tumbes",
        13: "Lambayeque",
        14: "Amazonas",
        15: "Ica",
        16: "Moquegua",
        17: "Junín",
        18: "Cusco",
        19: "Cajamarca",
        20: "Áncash",
        21: "Pasco",
        22: "Huancavelica",
        23: "Arequipa",
        24: "Apurímac",
        25: "Callao"
    }
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
    año = input("Ingrese el año: ")
    if int(año) < 2017 or int(año) > 2023:
        print("Año inválido. Ingrese un año válido de cuatro dígitos.")
        return
    
    mes = input("Ingrese el mes (1-12): ")
    if int(mes) not in range(1, 13):
        print("Mes inválido. Ingrese un número de mes válido (1-12).")
        return
    departamento = input("Ingrese el departamento (1-25): ")           
    if int(departamento) in range(1, 26):
        print("Departamento inválido. Ingrese un número de departamento válido (1-25).")
        return

    departamento_label = departamentos.get(int(departamento), "Desconocido")
    mes_label = meses.get(int(mes), "Desconocido")
    
    data_filtered = data[
        (data['Año de los casos'] == int(año)) &
        (data['Mes'] == int(mes)) &
        (data['Departamento'] == departamento_label)
    ]
    centros_mas_utilizados = data_filtered['Centro utilizado'].value_counts()
    plt.title(f'Centros mas utilizados en casos de violencia sexual en {mes_label}/{año}, {departamento_label}')
    centros_mas_utilizados.plot(kind='pie', figsize=(8,6), autopct='%1.1f%%')
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

def mostrar_todos_los_datos_ordenados():
    #NOSECOMOPONER LOS DATOS ORDENADOS

def cerrar_programa():
    print("Cerrando el programa...")
    

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Instrucciones del menú")
        print("2. Mostrar estadísticas")
        print("3. Mostrar todos los datos ordenados")
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