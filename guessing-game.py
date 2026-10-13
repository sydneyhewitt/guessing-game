import random # Used for generating a random number

# Game valid
game = True     # game status used to track whether the game should run or not

# Creating random number
random_num = random.randint(1, 10)      # generate a random numbe rand store it in a variable

# Creating guess list
previous_guesses = []       # create a list to store previous guesses

# Game Loop
while game == True:     # while loop for game so it continues to run until the player guesses the number

    print("\nPrevious Guesses: " + str(previous_guesses))       # Display the user's previous guesses
    guess = int(input("Guess a number between 1-10: "))     # Ask the user for a number between 1 and 10


    # Checking for Duplicates
    duplicate = False

    for g in previous_guesses:      # Use a for loop in order to make sure no duplicates are added to the previous_guesses list
        if g == guess:
            duplicate = True

    # While loop checking if valid

    while guess <= 0 or guess > 10 or guess in previous_guesses:        # while loop to check if the input is valid or not
        
        if guess <= 0 or guess > 10:        # Checks whether or not the guess was below 0 or above 10 and if it is display as invalid input
            print("\nInvalid input!")
        else:
            print("\nYou already guessed " + str(guess) + "!")      # if the guess is already in previous guesses, displays that to the user
            print("Choose a different number.")
        
        print("\nPrevious Guesses: " + str(previous_guesses))
        guess = int(input("Guess a number between 1-10: "))

    previous_guesses.append(guess)      # Adds guesses to the previous guesses list

    # Checking if they won

    if guess == random_num:     # Checking if the guess is correct
        print("\nYou guessed correctly!")
        game = False
    elif guess > random_num:
        print("\nTry again! The number is lower. ")
    elif guess < random_num:
        print("\nTry again! The number is higher. ")
