import random

class GuessingGame:
    """
    I chose to include a class to organize my code and to keep everthing
    centrailized.
    """

    # Generate a random number between 1-10 and store it in a variable
    number = random.randint(1, 10)
    print(number)

    """
    Generate a message to the user asking their name. For better improvement 
    on the project I implemented simple error handling to control if the  
    input is not a string. The program will quit if the user does not provide the
    proper input.
    """
    user = input("Enter your name:")

    if type(user) == str:
        print(f"Okay {user} I will guess a number between 1 and 10. You will "
              f"have 5 chances to guess the number. ENTER A NUMBER TO BEGIN!")

        guesses = 0

        if type(guesses) is int:
            while guesses < 5:
                guesses = int(input())
        else:
            print("Please enter a valid name (it must be of type string).")
            quit()

    else:
        print("Please enter a valid name (it must be of type string).")
        quit()



