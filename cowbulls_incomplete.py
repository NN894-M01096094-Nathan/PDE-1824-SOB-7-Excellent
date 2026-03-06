import random

def compare_numbers(number, user_guess):

    if len(user_guess) > 4:
        print("You've entered a number that has more than 4 digits!")
        print("Evaluating number of cows from left to right...")
        print("Any other numbers after the 4th digit are ignored!")

    cow = 0
    bull = 0

    for i in range(4):
        if number[i] == user_guess[i]:
            bull += 1
        else:
            cow +=1

    cowbull = [cow, bull]

    return cowbull # array with two elements: 0th being cow and 1st being bull

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") # raw_input is now redundant in 3.x
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    # Moved print statement to the else block... (Not an error, just to make it look better)

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
