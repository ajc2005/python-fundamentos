cats = [
    ["Nombre", "Edad", "Color"],
    ["Luna", "3", "gris"],
    ["Simba", "2", "naranja"],
    ["Michi", "5", "blanco y negro"],
    ["Neko", "1", "negro"]
]

print("Guardando información de gatos como csv...")
try:
    with open("gatos.csv", "w", encoding="utf-8") as csv_file:
        for cat in cats:
            line = ",".join(cat) + "\n"
            csv_file.write(line)

    print("Archivo gatos.csv creado correctamente.")

except Exception as e:
    print(f"Error al guardar el archivo: {e}")

print("\nContenido del archivo gatos.csv:")
try:
    with open("gatos.csv", "r", encoding="utf-8") as read_file:
        for line in read_file:
            print(line.strip())
except FileNotFoundError:
    print("Error: No se encontró el archivo gatos.csv")