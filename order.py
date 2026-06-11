"""
Task 8.1 Data Classes and Enums
"""

__author__ = "Kasra Asarroodi"


from dataclasses import dataclass
from enum import Enum


class CoffeeType(Enum):
   """Represents the different types of coffee available"""
   ESPRESSO = "Espresso"
   LONG_BLACK = "Long Black"
   LATTE = "Latte"
   CAPPUCCINO = "Cappuccino"
   MOCHA = "Mocha"


@dataclass
class Order:
    """ Represents an individual coffee order """
    name: str
    coffee_type: CoffeeType
    sugars: int
    upsize: bool 
     
   

    def __str__(self) -> str:
        if self.upsize :
          size = "Large"
        else:
          size = "Regular"
          
      
        if self.sugars == 1:
           sugar_word = "sugar"
        else:
           sugar_word = "sugars"
    
        return f"Order for {self.name}: {size} {self.coffee_type.value} with {self.sugars} {sugar_word}"


def input_coffee_type() -> CoffeeType:
    """
    Recieves the Coffee type by the user and returns the corresponding Coffeetype value.
    """
    selected_coffee = False 
    while not selected_coffee : 
        print ("Which coffee would you like?")  
        print("1. Espresso")
        print("2. Long Black")
        print("3. Latte")
        print("4. Cappuccino")
        print("5. Mocha")
        choice = input("Choice:")
        if choice == "1":
          selected_coffee = CoffeeType.ESPRESSO
        elif choice == "2":
          selected_coffee = CoffeeType.LONG_BLACK
        elif choice == "3":
            selected_coffee = CoffeeType.LATTE
        elif choice == "4":
            selected_coffee = CoffeeType.CAPPUCCINO
        elif choice == "5":
            selected_coffee = CoffeeType.MOCHA
        else:
            print("Invalid selection.")
    return selected_coffee


def input_order() -> Order:
    """
    Prompts the user with the necessary information to create an order summary.
    """
    name = input("Enter your name: ")
    coffee_type = input_coffee_type()
    sugars = int(input("How many sugars? "))
    while sugars < 0:
        print("Sugars we can't add negative sugars ;-)")
        sugars = int(input("How many sugars? "))
    upsize_input = input("Would you like to upsize? (y/n): ").lower()
    while upsize_input not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        upsize_input = input("Would you like to upsize? (y/n): ").lower()
    upsize = upsize_input == 'y'

    return Order(name, coffee_type, sugars, upsize)


def main():
    order : Order
    order = input_order()
    print(order)


if __name__ == "__main__":
    main()
