"""
Cálculo de Índice de Masa Corporal (IMC)
Descripción: Utiliza Numpy para calcular el IMC a partir de datos de altura y peso.
Ejemplo: Dado un array con pesos en kilogramos y otro con alturas en metros, calcular el IMC para cada persona.
"""

#Importamos los paquetes de numpy, pandas y matplotlib, datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from datetime import datetime

#Generar pesos aletorios
pesos = np.random.uniform(50,100,1000)

#round = limita los valores a 2 decimales, depende del valor que le pasemos
pesos_limitados = np.round(pesos,2)


#Generar alturas aleatorias
alturas = np.random.uniform(1.50, 2.10,1000)
alturas_limitadas = np.round(alturas, 2)


"""Formula de IMC
IMC = PESO / ALTURA ** 2
"""

IMC= pesos_limitados / (alturas_limitadas**2)
IMC_round = np.round(IMC,2)

#Crear listas para los pesos
peso_inferior, peso_normal, peso_superior, obesidad = [], [], [], []

#Listas para almacenar los datos en un archivo CSV
lista_archivo = []
lista_archivo_texto = []

#Declaracion de diccionario para manipular los datos en un grafico
dict_pesos = { }

#Ciclo para comprobar el IMC de cada persona
for imc in IMC_round:
    if imc <= 18.5:
        #print(f"Peso inferior al normal: {imc}")
        peso_inferior.append(imc)
        lista_archivo_texto.append("Peso inferior al normal")
        lista_archivo.append(imc)

    elif imc >= 18.5 and imc <= 24.9:
            #print(f"Peso normal: {imc}")
            peso_normal.append(imc)
            lista_archivo_texto.append("Peso normal")
            lista_archivo.append(imc)

    elif imc >= 25 and imc <= 29.9:
           # print(f"Peso superior al normal: {imc}")
            peso_superior.append(imc)
            lista_archivo_texto.append("Peso superior al normal")
            lista_archivo.append(imc)
    else:
        #print(f"Obesidad: {imc}")
        obesidad.append(imc)
        lista_archivo_texto.append("Obesidad")
        lista_archivo.append(imc)

#Almacenar las listas en un diccionario
dict_pesos["peso_inferior"] = peso_inferior
dict_pesos["peso_normal"] = peso_normal
dict_pesos["peso_superior"] = peso_superior
dict_pesos["obesidad"] = obesidad

#Elementos para usarlos en matplotlib
lista_titulos_pesos = ["Menos de 18.5", "18.5 - 24.9", "25.0 - 29.9", "Más de 30.0"]
lista_cantidad_pesos = [len(dict_pesos["peso_inferior"]),len(dict_pesos["peso_normal"]),
                        len(dict_pesos["peso_superior"]),len(dict_pesos["obesidad"])]
titulos = ["Peso inferior", "Peso normal", "Peso superior", "Obesidad"]



#Creando un Dataframe
data = {"Composicion Corporal": titulos, "Cantidad de personas": lista_cantidad_pesos}
dataframe_pesos = pd.DataFrame(data)
print(dataframe_pesos)

df_archivo = {"Composicion Corporal":lista_archivo_texto, "IMC": lista_archivo}
df_csv = pd.DataFrame(df_archivo)

#Creacion de la fecha actual
date = datetime.now()
year = date.year
month = date.month
day = date.day
df_csv.to_csv(f"{day}-{month}-{year}-Dataset_IMC.csv", index=False)
print("El archivo se ha creado correctamente...")

#Creamos el grafico usando matplotlib
barras = plt.bar( lista_titulos_pesos, lista_cantidad_pesos,  color="blue")
# es bar, porque es un grafico de barras

#Agregamos las etiquetas y titulos
plt.ylabel("Cantidad de personas")
plt.xlabel(" Promedio de Índice de Masa Corporal de 500 personas ")
plt.title("Distribución de pesos por cantidad de personas")


#Mostrar numeros en las barras
for barra, cantidad in zip(barras,lista_cantidad_pesos ):
    plt.text(barra.get_x() + barra.get_width() / 2,
             barra.get_height(),cantidad, ha="center", va="bottom")

#1000 es para indicar en el eje y, la cantidad de personas
plt.plot(1000,label="Cantidad de personas")
plt.legend()


#cambiar  texto que aparece  en matplotlib
plt.gcf().canvas.manager.set_window_title("Gráfico para el Indicador de IMC por grupo de personas")

#cambiar el icono
manager = plt.get_current_fig_manager()
manager.window.iconbitmap("../Proyecto-01/heart.ico")


#mostrar el grafico
plt.show()