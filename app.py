import os
from PIL import Image

# Funcion para listar los formatos permitidos
def listar_formatos():
    formatos = ["PNG", "JPG", "JPEG", "WEBP", "GIF", "BMP", "TIFF"]
    # Iteramos sobre cada elemento de la lista para imprimirlos en diferente linea
    print("Formatos Soportados:")
    for formato in formatos:
        print(f"- {formato}")

# Funcion para convertir una imagen
def convertir_imagen(ruta_imagen, formato_salida, directorio_destino=None):
    try:
        # Verificar si la imagen existe
        if not os.path.isfile(ruta_imagen):
            print(f"La imagen {ruta_imagen} no existe.")
            return None
        
        # Abrir la imagen
        imagen = Image.open(ruta_imagen)

        # Obtener informacion de la imagen original
        nombre_fichero = os.path.basename(ruta_imagen)
        # Separamos el nombre de la extension
        nombre_base = os.path.splitext(nombre_fichero)[0]

        # Determinar directorio de destino
        if directorio_destino is None:
            directorio_destino = os.path.dirname(ruta_imagen)

        # Crear directorio de destino si no existe
        if not os.path.exists(directorio_destino):
            os.makedirs(directorio_destino)

        # Crear la ruta de salida
        formato_salida = formato_salida.lower().strip(".")
        ruta_salida = os.path.join(directorio_destino, f"{nombre_base}.{formato_salida}")

        # Guardar la imagen convertida
        imagen.save(ruta_salida)
        print(f"Imagen convertida y guardada en {ruta_salida}")
        return ruta_salida
    
    except Exception as e:
        print(f"Error al convertir la imagen: {e}")
        return None
    
# Funcion para convertir multiples imagenes
def convertir_multiples_imagenes(directorio_origen, formato_salida, directorio_destino=None):

    """
    return: El numero de imagenes convertidas exitosamente (int)

    """
    
    # Verificar que el directorio existe
    if not os.path.exists(directorio_origen):
            print(f"La carpeta {directorio_origen} no existe.")
            return 0
    
    # Extensiones de imagenes
    extensiones_imagen = [".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff"]

    # Contador de imagenes convertidas
    contador = 0

    # Iterar por todos los ficheros en el directorio
    for fichero in os.listdir(directorio_origen):
        ruta_fichero = os.path.join(directorio_origen, fichero)

        # Verificar si es un fichero y tiene una extension soportada
        if os.path.isfile(ruta_fichero) and any(fichero.lower().endswith(ext) for ext in extensiones_imagen):
            
            # Convertir la imagen
            if convertir_imagen(ruta_fichero, formato_salida, directorio_destino):
                contador += 1
                
    return contador

# Funcion principal
def main():
    print("####### Conversor de Imágenes #######")

    # Mostrar formatos soportados
    listar_formatos()
    print("\n")

    # Menu de opciones
    print("Opciones:")
    print("1. Convertir una imagen")
    print("2. Convertir todas las imágenes de una carpeta")

    # Recogemos el imput del usuario
    opcion = int(input("\nSelecciona una opción (1-2): "))

    if opcion == 1:

        # Convertir una sola imagen
        ruta_imagen = input("Ingresa la ruta de la imagen a convertir: ")
        formato_salida = input("Ingresa el formato de salida (ej: PNG): ")
        directorio_destino = input("Ingresa la carpeta de destino (si se deja en blanco se usará la misma de la imagen): ")

        if not directorio_destino:
            directorio_destino = None

        convertir_imagen(ruta_imagen, formato_salida, directorio_destino)

    elif opcion == 2:

        # Convertir multiples imagenes
        directorio_origen = input("Ingresa la ruta de la carpeta con las imágenes a convertir: ")
        formato_salida = input("Ingresa el formato de salida (ej: PNG): ")
        directorio_destino = input("Ingresa la ruta de la carpeta de destino. Si no se ingresa ninguna, se creará una en el mismo directorio que las imágenes")

        if not directorio_destino:
            directorio_destino = None

        num_convertidas = convertir_multiples_imagenes(directorio_origen, formato_salida, directorio_destino)
        print(f"\nConvertidas {num_convertidas} imágenes con éxito.")

    else:
        print("Opción no válida. Por favor, ingrese 1 o 2")

main()