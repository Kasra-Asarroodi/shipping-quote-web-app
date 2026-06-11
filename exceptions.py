"""
Task 10.1 Exception handling
"""

__author__ = "Kasra Asarroodi"


from os import path


def number_input():
    """
    Runs the number input and parsing example.
    """
    keep_going: bool = True
    collected: list[int] = []
    num: int

    print("\nNumber Parsing Example")
    while keep_going:
        try:
         num = read_an_int("Enter an integer to add to the collection")
         collected.append(num)
         keep_going = input("Add another? (y/n) ").lower() == "y"
        except ValueError:
            print("cannot interpret input as a number")

    print(f"You entered these valid integer values: {collected}")


def list_access():
    """
    Runs the list access example.
    """
    keep_going: bool = True
    data: list[int] = [7, 3, 9, 2, 4]
    index: int

    print("\nList Access Example")
    while keep_going:
        try:
            index = read_an_int("Enter an index to view")
            print(f"The value at position {index} is {data[index]}")
            keep_going = input("Inspect another? (y/n) ").lower() == "y"
        except IndexError as ex:
            print(f"couldnt read that position  : {ex}")
            keep_going = input("Inspect another? (y/n) ").lower() == "y"


def read_file():
    """
    Runs the file reading example.
    """
    filename: str = input("Enter a file name in the current directory: ")
    try:
        file = open(f"{path.dirname(__file__)}/{filename}", "r")
        print(f"Contents of {filename}:")
        print(file.read())
        file.close()
    except UnicodeDecodeError as e:
        print(f"Cant read that file type: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    
        

    

def read_an_int(query: str) -> int:
    """
    Part of the number input and list access examples.
    """
    is_valid: bool = False
    value: int

    while not is_valid:
        value = int(input(f"{query}: "))
        is_valid = True

    return value


def main():
    choice: str = ""
    while choice != "Q" and choice != "q":
        print("1. Number input")
        print("2. List access")
        print("3. Read file")
        print("Q. Quit")
        choice = input("Action: ")
        match choice:
            case "1":
                number_input()
            case "2":
                list_access()
            case "3":
                read_file()
            case _:
                print("Unknown option")


if __name__ == "__main__":
    main()
