from collections import defaultdict
import re
from datetime import datetime

def analizar_logs(input_path, output_path):
    daily_view = defaultdict(int)
    
    try:
        with open(input_path, "r", encoding="utf-8") as cat_view_file:
            for line in cat_view_file:
                match = re.search(r'\d{4}-\d{2}-\d{2}', line)
                if match:
                    date = match.group()
                    daily_view[date] += 1
        
        date_order = sorted(daily_view.keys())
        
        with open(output_path, "w", encoding="utf-8") as sort_views_file:
            sort_views_file.write("Fecha,Visitas\n")
            for date in date_order:
                sort_views_file.write(f"{date},{daily_view[date]}\n")
                
        print(f"Resumen guardado")
        
        total_view = sum(daily_view.values())
        print(f"\nEstadísticas:")
        print(f"Total de días: {len(daily_view)}")
        print(f"Total de visitas: {total_view}")
        
        if daily_view:
            avg = total_view / len(daily_view)
            print(f"Promedio de visitas por día: {avg:.2f}")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    all_views = "visitas.log"
    views_short = "resumen_visitas.csv"
    
    print(f"Analizando archivo de logs...")
    analizar_logs(all_views, views_short)