class Air_company:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_profit(self):
        total = 0
        for flight in self.flights:
            total += flight.profit()
        return total

class Flight:
    def __init__(self, distance):
        self.distance = distance
        self.airplane = None
        self.staff = []
        self.tickets = []

    def set_airplane(self, airplane):
        self.airplane = airplane

    def add_staff(self, staff):
        self.staff.append(staff)

    def add_ticket(self, ticket):
        if self.airplane.capasity > len(self.tickets):
            self.tickets.append(ticket)
        else:
            raise Exception("Capasity error")

    def profit(self):
        total = 0
        for ticket in self.tickets:
            total += ticket.price
        for staff in self.staff:
            total -= staff.salary
        total -= self.airplane.consumption * self.distance * self.airplane.fuel.price
        return total

class Airplane:
    def __init__(self, capasity, fuel, consumption):
        self.capasity = capasity
        self.fuel = fuel
        self.consumption = consumption

class Staff:
    def __init__(self, salary):
        self.salary = salary

class Fuel:
    def __init__(self, price):
        self.price = price

class Ticket:
    def __init__(self, price):
        self.price = price


if __name__ == "__main__":
    ticket = Ticket(450)                    # $ one way
    fuel = Fuel(0.52)                       # $ per liter
    crew = Staff(2600)                      # crew salarie per flight combined. 20$/hour * 13 crew members * 10 hours
    boeing_777 = Airplane(314, fuel, 6800)  # n of seats, fuel, fuel consumption 6800 liters/hour
    flight682 = Flight(10)                  # hours of flight
    flight682.set_airplane(boeing_777)
    flight682.add_staff(crew)

    for i in range(boeing_777.capasity):
        flight682.add_ticket(ticket)

    KLM = Air_company()
    KLM.add_flight(flight682)

    print(f'Expenses are:\nCrew salarie per flight\t\t{crew.salary}$.\nFuel burned           \t\t{flight682.distance*boeing_777.consumption} liters.\nCost of burned fuel is\t\t{int(flight682.distance*boeing_777.consumption*fuel.price)}$.')
    print(f'KLM profit on flight682 is\t{int(KLM.total_profit())}$.')