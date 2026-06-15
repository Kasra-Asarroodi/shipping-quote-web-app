"""
6.1 Words
"""
__author__ = "Kasra Asarroodi"
def add_word(word_list: list[str], word: str):
    """
     Adds a new word to the word list if there is capacity and
   the word is not empty.
    """
    if word == "":
        print("Empty words cannot be added to the word manager")
    elif word in word_list:
        print(f" The word manager already contains '{word}.'")
    else:
     word_list.append(word)



def display_words(word_list: list[str]):
     """
     Displays all words in the word list, separated by a comma.
     """
     if len(word_list) == 0:
            print("The word manager is empty.")
     else:
        print(", ".join(word_list))



def average_word_length(word_list: list[str]) -> float:
    if len(word_list) == 0:
        print ("The word manager is empty.")
        return 0.0  
    else:
        total_length = sum(len(word) for word in word_list)
        return total_length / len(word_list)


def main(): 
    words: list[str] = [] # The collection of words in the word manager
    choice: str = "" # The user's menu choice
    new_word: str = "" # A new word to add, provided by the user

    print(r" __ __ __ __ ")
    print(r"| | / \ |__) | \ /__`")
    print(r"|/\| \__/ | \ |__/ .__/")
    
    while choice != "Q":
        print()
        print("1. Add a word")
        print("2. Display all words")
        print("3. Display word length")
        print("Q. Quit")
        
        choice = input("Choose an option (1, 2, 3, Q): ").upper()
        
        if choice == "1":   
            new_word = input("Enter a new word: ")
            add_word(words, new_word)
        elif choice == "2":
            display_words(words)
        elif choice == "3":
            print(f" Average word length: {average_word_length(words)}")
        elif choice == "Q":
            print("Goodbye!")
        else:
            print(f"Unknown option: {choice}")
if __name__ == "__main__":
     main()
  