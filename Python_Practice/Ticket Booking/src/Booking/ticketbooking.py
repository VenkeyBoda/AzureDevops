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
                ticket_(id (str): ticket_id
                passenger_name (str): passenger_name
                journey_date (init): journey_date
            """
            self._ticket_id = ticket_id
            self._passenger_name = passenger_name
            self._journey_date = journey_date

        @property
        def ticket_id(self):
            """Getter property for ticket id

            Returns:
                str: Ticket id
            """
            return self._ticket_id
        
        @property
        def passenger_name(self):
            """Getter property for passenger name

            Returns:
                   str: paassenger name
            """
            return self._passenger_name
        
        @property
        def journey_date(self):
            """Getter property for journey name

            Returns:
                 init: Journey date
            """
            return self._journey_date

class Book_Ticket:
     
        """this class is used for ticket confirm details

        Args:
            ticket_id (str): ticket_id
            passenger_name (str): passenger_name
            journey_date (init): journey_date
            bus_number (str): bus_number
            seat_number (str): seat_number

        """    
        def __init__(self, ticket_id, passenger_name, journey_date, vehicle_number, seat_number):
            """confirmation of bus and ticket details

            Args:
                ticket_id (str): ticket_id
                passenger_name (str): passenger_name
                journey_date (init): journey_date
                bus_number (str): vehicle_number
                seat_number (str): seat_number
         """
            
            self._ticket_id = ticket_id
            self._passenger_name = passenger_name
            self._journey_date = journey_date
            self._vehicle_number = vehicle_number
            self._seat_number = seat_number
            
        def display_ticket_info(self):
            """carrying soft copy or digitally

            """
            print(f"ticket id: {self._ticket_id}")
            print(f"passenger name: {self._passenger_name}")
            print(f"journey date: {self._journey_date}") 
            print(f"bus number: {self._vehicle_number}") 
            print(f"seat number: {self._seat_number}")

        def calculate_fare(self):
            """fare calculation based on seat class
            """
            fare_chart = { 
                 'AC': 700,
                 'Non-AC': 500,
                 'Express': 250,
                 'ordinary': 150
            }
            return fare_chart.get(self._seat_number, 0)
