# ------------------------------------------------------
#        Name: Aline Valenzuela-Lucero
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"
secret_word_2 = "Food"

# Task 1
def check_text():
    """ Add your docstring """
    sentence = input("Give me a sentence:")
    while secret_word not in sentence and secret_word_2 not in sentence:
        print("Try again")
        sentence = input("Give me another sentence:")
    print(f"You used the secret word!")
        



# Task 2
def check_greater():
    """ Add your docstring """
    pass



# Task 3
def get_special_numbers():
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
