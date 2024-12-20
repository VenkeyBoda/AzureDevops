"""    ticketbooking.py

    This module contains the base implementation of ticket booking

"""
class Ticket:
  
        """this class is used for ticket reservations

        Args:
            ticket_id (str): ticket_id
            passenger_name (str): passenger_name
            journey_date (init): journey_date

        """
        def __init__(self, ticket_id, passenger_name, journey_date):
            """initialize the ticket reservation

            Args:
                ticket_(id (init): ticket_id
                passenger_name (str): passenger_name
                journey_date (init): journey_date
            """
            self.ticket_id = ticket_id
            self.passenger_name = passenger_name
            self.journey_date = journey_date

        def display_ticket_info(self):
            """shown for the ticket to responsible person
            """
            print(f"ticket_id: {self.ticket_id}")
            print(f"passenger_name: {self.passenger_name}")
            print(f"journey_date: {self.journey_date}")

class BusTicket:
     
        """this class is used for ticket confirm details

        Args:
            ticket_id (init): ticket_id
            passenger_name (str): passenger_name
            journey_date (init): journey_date
            bus_number (str): bus_number
            seat_number (init): seat_number

        """    
        def __init__(self, ticket_id, passenger_name, journey_date, bus_number, seat_number):
            """confirmation of bus and ticket details

            Args:
                ticket_id (init): ticket_id
                passenger_name (str): passenger_name
                journey_date (init): journey_date
                bus_number (str): bus_number
                seat_number (init): seat_number
         """
        def display_ticket_info(self):
            """carrying soft copy or digitally

            """
            print(f"ticket id: {self.ticket_id}")
            print(f"passenger name: {self.passenger_name}")
            print(f"journey date: {self.journey_date}") 
            print(f"bus number: {self.bus_number}") 
            print(f"seat number: {self.seat_number}")

        def calculate_fare(self):
            """fare calculation based on seat class
            """
            fare_chart = { 
                 'AC_bus': 700,
                 'luxury': 500,
                 'Express': 250,
                 'ordinary': 150
            }
            return fare_chart.get(self.seat_number, 0)
