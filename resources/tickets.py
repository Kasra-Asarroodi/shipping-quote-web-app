"""
Task 4.1 Selection
"""

__author__ = "Kasra Asarroodi"

from ast import Add


ADULT_PRICE = 24.00
CHILD_PRICE = 17.80
STUDENT_PRICE = 19.40
SENIOR_PRICE = 15.00
SURCHARGE_EVENING = 2.00
SURCHARGE_WEEKEND = 3.00
SURCHARGE_GOLD = 7.50
SURCHARGE_IMAX = 4.25
BOOKING_FEE = 1.75


def display_heading(heading: str):
    """
    Displays the given heading in ALL CAPS, underlined above and below
    by equals (=) symbols, and then followed by a blank line.
    """
    print("=" * len(heading.upper()))
    print(heading.upper())
    print("=" * len(heading.upper()))
    print()


def format_cost(cost: float) -> str:
    """
    Return a given cost formatted as currency string ($dd.cc). If the cost
    is 5.00 or greater, the returned string includes the GST contribution.
    """
    gst: float= 0.0    
    formatted_cost: str = f"${cost:.2f}"
    if cost >= 5.00:
        gst = cost * 0.10
        formatted_cost += f" (GST ${gst:.2f})"
        
        return formatted_cost


    # TODO: Complete the implementation of this function


def get_ticket_price() -> float:
    """
    Prompts the user for a ticket type. Returns the ticket price if a valid
    option is selected or the base (Adult) ticket price otherwise.
    """
    ticket_type: int # The type of ticket
    print("1. Adult")
    print("2. Child")
    print("3. Student")
    print("4. Senior")
    
    ticket_type = int(input("Choose a ticket type (1-4): "))  
    
    ticket_price: float = 0.0 # The cost of the ticket
    if ticket_type == 1:
       ticket_price = ADULT_PRICE
       print(f"> Adult ticket price: {format_cost(ticket_price)}")
    elif ticket_type == 2:
       ticket_price = CHILD_PRICE
       print(f"> Child ticket price: {format_cost(ticket_price)}")
    elif ticket_type == 3:
        ticket_price = STUDENT_PRICE
        print(f"> Student ticket price: {format_cost(ticket_price)}")
    elif ticket_type == 4:
        ticket_price = SENIOR_PRICE
        print(f"> Senior ticket price: {format_cost(ticket_price)}")
    else:
        print(f">Invalid ticket type: {ticket_type}")
        print(f"> Defaulting to Adult ticket: {format_cost(ADULT_PRICE)}")
        ticket_price = ADULT_PRICE

    return ticket_price


def get_ticket_surcharges() -> float:
    """
    Prompts the user for ticket preferences. Returns the total surcharge.
    """
    day: str = input("Day (weekday/weekend): ").lower()
    surcharge: float = 0.0 # The calculated ticket surcharge
    if (day) == "weekend": 
        surcharge += SURCHARGE_WEEKEND
        print(f"> Weekend surcharge: {format_cost(SURCHARGE_WEEKEND)}")
    elif (day) == "weekday":
        print(f"> No surcharge for weekdays")
    else:
        print(f"> Unknown option: {day}")

    time: str = input("Time (matinee/evening): ").lower()
    if (time) == "evening":
        surcharge += SURCHARGE_EVENING
        print(f"> Evening surcharge: {format_cost(SURCHARGE_EVENING)}")
    elif(time) == "matinee":
        print(f"> No surcharge before 5pm")
    else:
        print(f"> Unknown option: {time}")
    
    Experience: str = input("Experience (standard/gold/IMAX): ").lower() # The cinema experiences
    if (Experience) == "gold":
        surcharge += SURCHARGE_GOLD
        print(f"> Gold Class surcharge: {format_cost(SURCHARGE_GOLD)}")
    elif (Experience) == "imax":
        surcharge += SURCHARGE_IMAX
        print(f"> IMAX surcharge: {format_cost(SURCHARGE_IMAX)}")
    elif (Experience) == "standard":
        print(f"> No surcharge for standard experience")
    else:
        print(f"> Unknown option: {Experience}")
        
  
    return surcharge


def main():
    ticket_price: float = 0.0 # The total cost of the ticket

    display_heading("Python Cinemas: Ticket Kiosk")
    print("Choose your ticket options...")
    print()

    ticket_price += get_ticket_price()
    ticket_price += get_ticket_surcharges()

    print()
    print(f"Ticket: {format_cost(ticket_price)}")
    print(f"Booking fee: {format_cost(BOOKING_FEE)}")

    ticket_price += BOOKING_FEE
    print()
    print(f"TOTAL: {format_cost(ticket_price)}")


if __name__ == "__main__":
    main()
