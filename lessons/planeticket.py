"""Class practice."""

class PlaneTicket:
    """Plane Ticket Class."""
    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost
        return None

    def __str__(self):
        return f"flight from {self.departure_city} to {self.arrival_city}, departure at: {self.departure_time} cost: {self.ticket_cost}"
    
    def delay(self, delay_hours: int):
        self.departure_time += delay_hours
        return None
    
    def discount(self, discount: float):
        self.ticket_cost = self.ticket_cost*(1-discount)
        return None

def find_cheapest_ticket(list: list[PlaneTicket]) -> PlaneTicket:
    cheapest_ticket = list[0]
    for ticket in list:
        if ticket.ticket_cost < cheapest_ticket.ticket_cost:
            cheapest_ticket = ticket 
    return cheapest_ticket

ticket1: PlaneTicket = PlaneTicket('denver', 'houston', 300, 20.00)
ticket2: PlaneTicket = PlaneTicket('durham', 'richmond', 300, 15.00)

print(str(ticket1))
ticket1.delay(300)
print(str(ticket1))
ticket1.discount(.1)
print(str(ticket1))
print(find_cheapest_ticket([ticket1, ticket2]))

