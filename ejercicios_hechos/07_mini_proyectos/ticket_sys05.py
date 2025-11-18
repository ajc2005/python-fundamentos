import json
from typing import Dict, List
from datetime import datetime

class TicketSys:
    def __init__(self, file: str = "tickets.json"):
        self.tickets: Dict[int, dict] = {}
        self.next_id = 1
        self.file = file
        self.load_tickets()
    
    def create_ticket(self, title: str, description: str) -> int:
        ticket = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "state": "active",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "expire": None
        }
        
        self.tickets[self.ne] = ticket
        self.siguiente_id += 1
        self.save_tickets()
        return ticket["id"]
    
    def list_tickets(self, only_active: bool = False) -> List[dict]:
        tickets = self.tickets.values()
        if only_active:
            tickets = [t for t in tickets if t["state"] == "active"]
        return list(tickets)
    
    def expire_ticket(self, ticket_id: int) -> bool:
        if ticket_id not in self.tickets:
            return False
        
        if self.tickets[ticket_id]["state"] == "expired":
            return False
        
        self.tickets[ticket_id]["state"] = "expired"
        self.tickets[ticket_id]["expire"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_tickets()
        return True
    
    def save_tickets(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump({"tickets": self.tickets, "next_id": self.next_id}, f, indent=2)
    
    def load_tickets(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tickets = data["tickets"]
                self.next_id = data["next_id"]
        except FileNotFoundError:
            self.tickets = {}
            self.next_id = 1

def mostrar_menu():
    print("\n=== Sistema de Tickets ===")
    print("1. Crear ticket")
    print("2. Listar tickets")
    print("3. Cerrar ticket")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    sys_tickets = TicketSys()
    
    while True:
        sel = mostrar_menu()
        
        if sel == "1":
            title = input("Título del ticket: ")
            description = input("Descripción: ")
            ticket_id = sys_tickets.create_ticket(title, description)
            print(f"Ticket creado con ID: {ticket_id}")
        
        elif sel == "2":
            only_active = input("¿Mostrar solo tickets abiertos? (s/n): ").lower() == 's'
            tickets = sys_tickets.list_tickets(only_active)
            print("\n=== Lista de Tickets ===")
            for t in tickets:
                print(f"ID: {t['id']} - {t['title']} ({t['state']})")
                print(f"Creado: {t['created']}")
                if t['expired']:
                    print(f"Caducado: {t['expired']}")
                print(f"Descripción: {t['description']}\n")
        
        elif sel == "3":
            try:
                ticket_id = int(input("ID del ticket a expirar: "))
                if sys_tickets.expire_ticket(ticket_id):
                    print("Ticket expirado correctamente")
                else:
                    print("No se pudo expirar el ticket")
            except ValueError:
                print("ID inválido")
        
        elif sel == "4":
            break
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()