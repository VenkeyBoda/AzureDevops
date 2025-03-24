"""
main.py

This is the main module which gets called when cli is used
"""

from Booking.ticketbooking import Book_Ticket

# Creating a standard bus ticket
ticket_details = Book_Ticket("B12356", "venkatesh", "2024-12-21", "TS10FF6852", "AC")
ticket_details.display_ticket_info()
print(f"Fare: {ticket_details.calculate_fare()}")