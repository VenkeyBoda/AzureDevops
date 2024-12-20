"""
main.py

This is the main module which gets called when cli is used
"""

from Booking.ticketbooking import BusTicket

# Creating a standard train ticket
standard_ticket = BusTicket("B12356", "venkatesh", "2024-12-20", "TS10FF6852", "luxury")
standard_ticket.display_ticket_info()
print(f"Fare: {standard_ticket.calculate_fare()}")