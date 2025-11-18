import statistics
from typing import List, Tuple
import json

class RefugioStats:
    def __init__(self, cats: List[Tuple[float, int]]):
        self.cats = cats
        self.weight = [weight for weight, _ in cats]
        self.age = [age for _ , age in cats]
    
    def calcular_estadisticas(self) -> dict:
        stats = {
            "total_cats": len(self.cats),
            "weight": {
                "media": statistics.mean(self.weight),
                "mediana": statistics.median(self.weight)
            },
            "age": {
                "media": statistics.mean(self.age),
                "mediana": statistics.median(self.age)
            },
            "top_pesados": sorted(self.cats, reverse=True)[:3]
        }
        return stats
    
    def mostrar_resumen(self, stats: dict):
        """Muestra el resumen por pantalla"""
        print("\n=== Estadísticas del Refugio ===")
        print(f"Total de gatos: {stats['total_cats']}")
        
        print("\nEstadísticas de peso:")
        print(f"- Media: {stats['weight']['media']:.2f} kg")
        print(f"- Mediana: {stats['weight']['mediana']:.2f} kg")
        
        print("\nEstadísticas de edad:")
        print(f"- Media: {stats['age']['media']:.1f} años")
        print(f"- Mediana: {stats['age']['mediana']:.1f} años")
        
        print("\nTop 3 gatos más pesados:")
        for i, (weight, age) in enumerate(stats['top_pesados'], 1):
            print(f"{i}. {weight:.2f} kg ({age} años)")
    
    def guardar_resumen(self, stats: dict, file: str):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)
        print(f"\nResumen guardado en {file}")

def main():
    # Datos de ejemplo (peso en kg, edad en años)
    gatos_ejemplo = [
        (4.5, 3),
        (3.8, 2),
        (5.2, 5),
        (4.0, 1),
        (6.1, 4),
        (3.5, 2),
        (4.8, 6),
        (5.5, 3)
    ]
    
    shelter = RefugioStats(gatos_ejemplo)
    stats = shelter.calcular_estadisticas()
    
    shelter.mostrar_resumen(stats)
    
    shelter.guardar_resumen(stats, "estadisticas_refugio.json")

if __name__ == "__main__":
    main()