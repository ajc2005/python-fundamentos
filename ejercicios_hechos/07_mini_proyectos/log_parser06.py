from collections import defaultdict
from datetime import datetime
import re
from typing import Dict, List, Tuple

class ParserLogs:
    def __init__(self, input_file: str, output_file: str = "resumen.txt"):
        self.input_file = input_file
        self.output_file = output_file
        self.logs_by_type: Dict[str, int] = defaultdict(int)
        self.logs_by_date: Dict[str, int] = defaultdict(int)
    
    def read_lines(self, line: str) -> Tuple[str, str]:
        line_split = line.split()
        if len(line_split) >= 4: 
            date = line_split[0]
            type = line_split[2]
            return date, type
        return None, None
    
    def check_logs(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                for line in f:
                    date, type = self.read_lines(line.strip())
                    if date and type:
                        self.logs_by_date[date] += 1
                        self.logs_by_type[type] += 1
            return True
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo")
            return False
    
    def generar_resumen(self):
        if not self.logs_by_date or not self.logs_by_type:
            return "No hay datos para generar el resumen"
        
        resumen = []
        resumen.append("=== RESUMEN DE LOGS ===\n")
        
        resumen.append("EVENTOS POR TIPO:")
        for type, count in sorted(self.logs_by_type.items()):
            resumen.append(f"{type}: {count}")
        
        resumen.append("\nEVENTOS POR FECHA:")
        for date, count in sorted(self.logs_by_date.items()):
            resumen.append(f"{date}: {count}")
        
        total_events = sum(self.logs_by_type.values())
        resumen.append(f"\nTotal de eventos: {total_events}")
        resumen.append(f"Días diferentes: {len(self.logs_by_date)}")
        if self.logs_by_date:
            avg = total_events / len(self.logs_by_date)
            resumen.append(f"Promedio de eventos por día: {avg:.2f}")
        
        return "\n".join(resumen)
    
    def guardar_resumen(self):
        resumen = self.generar_resumen()
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(resumen)
            print(f"Resumen guardado en {self.output_file}")
            return True
        except Exception as e:
            print(f"Error al guardar el resumen: {e}")
            return False

def main():
    # Archivo de ejemplo (si no existe, crear uno)
    ejemplo_logs = [
        "2025-11-07 10:15:30 INFO Sistema iniciado",
        "2025-11-07 10:16:45 WARNING Espacio en disco bajo",
        "2025-11-07 11:20:15 ERROR Base de datos no responde",
        "2025-11-08 09:00:00 INFO Respaldo iniciado",
        "2025-11-08 09:30:00 INFO Respaldo completado",
        "2025-11-08 15:45:30 WARNING Memoria baja",
    ]
    
    # Crear archivo de logs de ejemplo
    with open("ejemplo.log", 'w', encoding='utf-8') as f:
        for log in ejemplo_logs:
            f.write(log + "\n")
    
    # Procesar logs
    parser = ParserLogs("ejemplo.log")
    if parser.check_logs():
        parser.guardar_resumen()
        # Mostrar resumen en pantalla también
        print("\n" + parser.generar_resumen())

if __name__ == "__main__":
    main()