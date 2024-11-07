import matplotlib.pyplot as plt

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
    archivo = open(nombre_archivo, "r", encoding='utf-8')  
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
    archivo = open(nombre_archivo, "r", encoding='utf-8')
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


def main():
    mostrar_mensaje() 
    nombre_archivo = "C:\\Users\\marie\\Downloads\\nasa_global_landslide_catalog_point (1).csv"

    archivo = open(nombre_archivo, 'r', encoding='utf-8')  
    print("Primeras 15 filas del archivo (sin incluir el encabezado):")
    mostrar_primeras_filas(archivo)
    archivo.close()  

    nombre_columna = input("\nIntroduce el nombre de la columna para calcular estadísticas (forma del objeto, aproximación de locación, contador de fatalidad, latitud, longitud, índice geográfico): ")
    calcular_estadisticas(nombre_archivo, nombre_columna)

    graficar = input("\nVer la grafica (si/no): ")
    if graficar.lower() == 'si':
        graficar_columna(nombre_archivo, nombre_columna)


if __name__ == "__main__":
    main()
