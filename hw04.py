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
    """ The code will ask the user to input a sentence. If the sentence does not contain the either secret word
        the while loop will cycle back and have the user try again. If the user managed to use the
        secret word, then the code will print that they used the seceret word."""
    sentence = input("Give me a sentence:") #user input
    while secret_word not in sentence and secret_word_2 not in sentence: #while loop that will cycle till the word is used
        print("Try again")
        sentence = input("Give me a sentence:")
    print(f"You used the secret word!") #result to using the secret word
        



# Task 2
def check_greater():
    """ Add your docstring """
    a1 = int(input("Give me a first integer:"))
    a2 = int(input("Give me a second integer:"))
    if a2 < a1:
        print("First is Greater")
    elif a1 < a2:
        print("Second is greater")
    else:
        print("Try again")
    print("Done")



# Task 3
def get_special_numbers():
    """ Add your docstring """
    range(1,41)
    for i in range(1,41):
        if i%2!=0 and i%3==0 and i%5!=0:
            print(i)
        
        


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
