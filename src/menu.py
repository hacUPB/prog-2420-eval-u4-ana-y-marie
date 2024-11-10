import os
import matplotlib.pyplot as plt

def listar_archivos():
        ruta = input("Ingrese la ruta de un directorio (Enter para el actual): ")
        ruta = ruta.strip('"')
        if ruta.strip() == "":
            ruta = os.getcwd()
        if os.path.isdir(ruta):
            print(f"Archivos en el directorio: '{ruta}'")
            archivos = os.listdir(ruta)
            if archivos: 
                for archivo in archivos:
                    print("archivo")
            else: 
                print("No se encontraron archivos en el directorio")
        else:
            print("La ruta es inválida.")  
        
def contar_palabras(archivo):
    if os.path.isfile(archivo):
        with open(archivo, "r", encoding='utf-8') as a:
            contenido = a.read()
            palabras = contenido.split()
            total_palabras = 0
            for palabra in palabras:
                total_palabras = total_palabras + 1
            print(f"El numero total de palabras encontradas en el archivo fueron: {total_palabras}")
    else: 
        print("No es un archivo válido.")
        
def reemplazar_palabras(archivo, palabra_de_interes, palabra_a_reemplazar):
    if os.path.isfile(archivo):
        with open(archivo, 'r', encoding='utf-8') as a:
            contenido2 = a.readlines()
        new_contenido = []
        for linea in contenido2:
            new_contenido.append(linea.replace(palabra_de_interes, palabra_a_reemplazar))
            
        with open(archivo, 'w', encoding='utf-8') as a:
            for linea in new_contenido:
                a.write(linea)
        
        print(f"Fue reemplazada '{palabra_de_interes}' por {palabra_a_reemplazar}")
    else:
        print("No es un archivo válido")
        
def contar_caracteres(archivo):
    if os.path.isfile(archivo):
        with open(archivo, 'r', encoding='utf-8') as a:
            contenido3 = a.read()
            total_caract = len(contenido3)
            caracteres_sin_espacio = len(contenido3.replace(" ",""))
            print(f"El total de caracteres con espacios es: {total_caract}")
            print(f"El total de caracteres sin incluir los espacios es: {caracteres_sin_espacio}")
    else:
        print("No es un archivo válido")

def menu_de_texto(archivo):
    while True:
        print("\nSubmenu para archivo de texto:")
        print("1. Contar número de palabras")
        print("2. Reemplazar una palabra por otra")
        print("3. Contar el número de caracteres")
        print("4. Salir")
        
        opcion = input("Elija una opción: ")
        if opcion == "1":
            contar_palabras(archivo)
        elif opcion == "2":
            palabra_de_interes = input("Ingrese la palabra a buscar: ")
            palabra_a_reemplazar = input("Ingrese la palabra de reemplazo: ")
            reemplazar_palabras(archivo, palabra_de_interes, palabra_a_reemplazar)
        elif opcion == "3":
            contar_caracteres(archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida, vuelva a intentarlo")

def mostrar_mensaje():
    info = ("Los datos mostrados en cada línea son: forma del objeto, "
            "aproximación de locación, contador de fatalidad, latitud, "
            "longitud e índice geográfico respectivamente de objetos estudiados "
            "del espacio en diversos países por la NASA.")
    print(info)

def mostrar_primeras_filas(archivo):
    encabezado = archivo.readline().strip().split(",")
    for i in range(15):
        linea = archivo.readline().strip()
        if not linea: 
            break 
        fila = linea.split(",") 
        columnas_para_mostrar = [fila[i] for i in [1, 10, 15, 22, 23, 28] if i < len(fila)]
        print(columnas_para_mostrar) 

def calcular_estadisticas(nombre_archivo, nombre_columna):
    datos = []
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        encabezado = archivo.readline().strip().split(",")
        
        establecer_nombres_columnas = {
            "forma del objeto": 1,
            "aproximación de locación": 10,
            "contador de fatalidad": 15,
            "latitud": 22,
            "longitud": 23,
            "índice geográfico": 28
        }
        
        if nombre_columna.lower() not in establecer_nombres_columnas:
            print("Esta columna no existe.")
            return None

        indice_columna = establecer_nombres_columnas[nombre_columna.lower()]

        for linea in archivo:
            fila = linea.strip().split(",")
            if len(fila) > indice_columna and fila[indice_columna].replace('.', '', 1).replace('-', '', 1).isdigit():
                datos.append(float(fila[indice_columna]))

    if datos:
        n_datos = len(datos)
        promedio = sum(datos) / n_datos
        datos.sort()
        mediana = (datos[n_datos // 2] if n_datos % 2 == 1 else 
                   (datos[n_datos // 2 - 1] + datos[n_datos // 2]) / 2)
        print("\nEstadísticas de la columna '" + nombre_columna + "':")
        print("Número de datos:", n_datos)
        print("Promedio:", promedio)
        print("Mediana:", mediana)
        print("Valor máximo:", max(datos))
        print("Valor mínimo:", min(datos))
    else:
        print("No se encontraron datos numéricos en la columna especificada.")

def graficar_columna(nombre_archivo, nombre_columna):
    datos = []
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        encabezado = archivo.readline().strip().split(",")
        
        establecer_nombres_columnas = {
            "forma del objeto": 1,
            "aproximación de locación": 10,
            "contador de fatalidad": 15,
            "latitud": 22,
            "longitud": 23,
            "índice geográfico": 28
        }

        if nombre_columna.lower() not in establecer_nombres_columnas:
            print("Esta columna no existe.")
            return None

        indice_columna = establecer_nombres_columnas[nombre_columna.lower()]

        for linea in archivo:
            fila = linea.strip().split(",")
            if len(fila) > indice_columna and fila[indice_columna].replace('.', '', 1).replace('-', '', 1).isdigit():
                datos.append(float(fila[indice_columna]))

    if datos:
        plt.figure(figsize=(10, 5))
        plt.plot(datos, linestyle='-', color='pink')
        plt.title(f'Gráfica de {nombre_columna}')
        plt.xlabel('Índice de datos')
        plt.ylabel(nombre_columna)
        plt.grid()
        plt.show()
    else:
        print("No se encontraron datos numéricos en la columna especificada para graficar.")

def menu_csv():
    mostrar_mensaje() 
    nombre_archivo = "C:\\Users\\marie\\Downloads\\nasa_global_landslide_catalog_point (1).csv"

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        print("Primeras 15 filas del archivo (sin incluir el encabezado):")
        mostrar_primeras_filas(archivo)

    nombre_columna = input("\nIntroduce el nombre de la columna para calcular estadísticas (forma del objeto, aproximación de locación, contador de fatalidad, latitud, longitud, índice geográfico): ")
    calcular_estadisticas(nombre_archivo, nombre_columna)

    graficar = input("\n¿Ver la gráfica? (si/no): ")
    if graficar.lower() == 'si':
        graficar_columna(nombre_archivo, nombre_columna)

def main():
    while True:
        print("\nMenú principal:")
        print("1. Listar archivos en la ruta actual o una ruta especificada.")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo CSV (.csv)")
        print("4. Salir")
        
        opcion = input("Por favor eliga una de las siguientes opciones: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            archivo = input("Ingrese la ruta del archivo: ")
            archivo = archivo.strip('"')
            menu_de_texto(archivo)
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            print("saliendo...")
            break
        else:
            print("Opcion no válida")

if __name__ == "__main__":
    main()


