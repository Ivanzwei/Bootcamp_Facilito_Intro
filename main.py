import shutil
from pathlib import Path

# Solicita al usuario el directorio que quiere ordenar.
current_path = Path.cwd()
directorio_path = input("Ingrese el nombre de la carpeta que desea ordenar. Si desea ordenar la carpeta en la que se encuentra el programa, escriba un punto '.'")

#Con el punto . se señala al directorio actual.
if directorio_path == ".":
    directorio_path = current_path
else:
    directorio_path = current_path / directorio_path

# Lista con extensiones para generar las carpetas.
extensiones = ["pdf", "jpg", "png", "txt"]

# Se generan las carpetas con las extensiones creadas en la lista anterior.
for extension in extensiones:
    carpeta = current_path / (extension + "s") # Se agrega la "s" para tener los nombres en plural. 
    if not carpeta.exists():
        carpeta.mkdir()

#Se recorren los archivos y se ordenan de acuerdo a su extensión.
def move_file(directory):

    for dir in directory.iterdir():
            if dir.is_dir():
               #move_file(dir)
               pass
            elif dir.is_file() and dir.suffix == ".txt":   
                shutil.move(dir, current_path / "txts")
            elif dir.is_file() and dir.suffix == ".pdf":   
                shutil.move(dir, current_path / "pdfs")
            elif dir.is_file() and dir.suffix == ".png":   
                shutil.move(dir, current_path / "pngs")

# Condicional que llama la función para clasificar archivos.
if directorio_path.exists:
    move_file(directorio_path)
else:
    print("El directorio que ingresó no existe.")

# Muestra las nuevas carpetas creadas.
for extension in extensiones:
    carpeta = current_path / (extension + "s")
    if carpeta.exists():
        print("Se ha creado la carpeta " + str(carpeta))

