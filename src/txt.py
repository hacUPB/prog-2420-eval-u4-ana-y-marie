import os 

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
        print("\n")
        print("Submenu para archivo de texto:")
        print("1. Contar numero de palabras")
        print("2. Reemplazar una palabra por otra")
        print("3. Contar el número de caracteres")
        print("4. salir")
        
        opcion_elegida = input("Eliga una de las opciones: ")
        if opcion_elegida == "1":
            contar_palabras(archivo)
        elif opcion_elegida == "2":
            palabra_de_interes = input("Ingrese la palabra a buscar: ")
            palabra_a_reemplazar = input("Ingrese la palabra de reemplazo: ")
            reemplazar_palabras(archivo, palabra_de_interes, palabra_a_reemplazar)
        elif opcion_elegida == "3":
            contar_caracteres(archivo)
        elif opcion_elegida == "4":
            break
        else:
            print("Opción no válida, vuelva a intentarlo")

def main():
    
    while True:
        print("\n")
        print("Menú principal:")
        print("1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos.")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivos separados por comas (.csv)")
        print("4. Salir")
        
        opcion = input("Por favor eliga una de las siguientes opciones: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            archivo = input("Ingrese la ruta del archivo: ")
            archivo = archivo.strip('"')
            menu_de_texto(archivo)
        elif opcion == "3":
            jji
        elif opcion == "4":
            print("saliendo...")
            break
        else:
            print("Opcion no válida")
       
if __name__ == "__main__":
    main()
           
        
        

            
                
            