# In this problem, you'll create a program that guesses a secret number!

print "Please think of a number between 0 and 100!"


def middle(a, b):
    return int((a + b) / 2.0)

# boundaries
low = 0
high = 100

while True:
    guess = middle(low, high)
    print "Is your secret number " + str(guess) + "?"
    answer = raw_input("Enter 'h' to indicate the guess is too high. "
                       "Enter 'l' to indicate the guess is too low. "
                       "Enter 'c' to indicate I guessed correctly. ")
    if answer == "c":
        print "Game over. Your secret number was: ", guess
        break
    elif answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    else:
        print "Sorry, I did not understand your input."
