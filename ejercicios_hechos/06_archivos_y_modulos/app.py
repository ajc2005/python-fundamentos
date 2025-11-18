import os
from utils03 import read_lines, save_lines

def main():
    file_path = input("Ingresa la ruta del archivo a leer: ")
    
    if not os.path.exists(file_path):
        print(f"Error: No se encontró ningún archivo con la ruta especificada")
        return
    
    try:
        print(f"\nLeyendo archivo:")
        lines = read_lines(file_path)
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line}")
        
        output_file = "file.txt"
        num_lines = [f"Línea {i}: {line}" for i, line in enumerate(lines, 1)]
        save_lines(output_file, num_lines)
        print(f"\nSe ha guardado una copia numerada en {output_file}")
        
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()