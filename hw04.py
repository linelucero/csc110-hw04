# ------------------------------------------------------
#        Name: Aline Valenzuela-Lucero
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ The code will ask the user to input a sentence. If the sentence does not contain the secret word or the word dog
        the while loop will cycle back and have the user try again. If the user managed to use the
        secret word, then the code will print that they used the seceret word. If the user uses the word dog, then a different
        response will be printed."""
    sentence = input("Give me a sentence: ") #user input
    while secret_word not in sentence: #while loop that will cycle till the word is used
        if "dog" in sentence or "Dog" in sentence: #dog conditional
            print("You used the word \"dog\" or the word \"Dog\"!")
            break #ends the loop
        else: #anything other than if conditional will ask the user to try again.
            print("Try again")
        sentence = input("Give me a sentence: ")
    if secret_word in sentence:
            print(f"You used the secret word!") #result to using the secret word
            


# Task 2
def check_greater():
    """ This function will ask the user to input two numbers for two different values. The conditional will compare both of the values,
        greater than, less than or equal. If greater/less than each other, a corresponding message will print as the result.
        if they are equal, the user will be asked to try again."""
    while True: #while loop runs if true
        a1 = int(input("Give me a first integer: ")) #input 1
        a2 = int(input("Give me a second integer: ")) #input 2
        if a2 < a1: #if comparison
            print("First is Greater")
            break
        elif a1 < a2: # if comparison
            print("Second is Greater")
            break
        else: #if they equal try again
            print("Try again")
    print("Done")



# Task 3
def get_special_numbers():
    """ This function takes a range of numbers 1-40, and selects those that are odd, multiples of 3 and not multiples of 5. then, they are
        each listed on their line"""
    range(1,41) #setting the number range
    for i in range(1,41): #takes each number in the range
        if i%2!=0 and i%3==0 and i%5!=0: #conditional if they are odd, multiple of 3 and not of 5
            print(i) #prints all the numbers
        
        


# Task 4.a
def my_for_loop():
    """ This function asks the user for a string, or a word. If the word is not within the desired range (2,5), the word will be taken
        as a bad word. If in the range, the code will label vowels and consonants using a for loop with conditionals."""
    word = str(input("Give me a string: ")) #user input
    ran = range(2,6) #word range
    for letter in word: #for loop to cycle the letters
        if len(word) in ran and " " not in word: #if the word meets the range and no spaces
            if letter in "aeiou": #conditional for vowels
                print(letter,"is a vowel")
            elif letter in "bcdfghjklmnpqrstvwxyz": #conditional for consonants.
                print(letter,"is a consonant")
        else: #if you didnt obey the range or spaces, then its a bad word
            print("bad word")
            return

# Task 4.b
def my_while_loop():
    """ using a while loop, the user is given a menu of letters to pick from. first, if the user does not pick from the correct values
        the user will have to  choose from the menu again. a will print the manu again, b will say goodbye and c will exit the program
        immediately."""
    letter = input("Choose one option: a, b, or c: ") #user input
    while letter == "a": #if a, then try again
        letter = input("Choose one option: a, b, or c: ")
    if letter == "b": #if b then good bye
        print("Goodbye")
    elif letter == "c": #if c then it exits
        exit()
    while letter in "defghijklmnopqrstuvwsyz": #any other letter then please try again within the while loop
        print("try again")
        letter = input("Choose one option: a, b, or c: ") #try again
        while letter == "a": #choosing a will allow you to choose from menu
            letter = input("Choose one option: a, b, or c: ")
    
        
        

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
