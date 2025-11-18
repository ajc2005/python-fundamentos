# Parte 1: Escribir archivo
print("Escribiendo archivo...")
with open("escribir.txt", "w", encoding="utf-8") as text_file:
    text_file.write("Primera línea\n")
    text_file.write("Segunda línea\n")
    text_file.write("Tercera línea\n")

print("Archivo creado correctamente.")

# Parte 2: Leer archivo
print("\nLeyendo archivo:")
try:
    with open("escribir.txt", "r", encoding="utf-8") as read_file:
        for i, line in enumerate(read_file, 1):
            print(f"{i}: {line.strip()}")
except FileNotFoundError:
    print("Error: No se encontró el archivo escribir.txt")