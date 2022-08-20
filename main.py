import random

def ComputerGuess(x):

    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too low [L] or too high [H] or correct [C] ?')
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
    print(f'yehh!! Computer guessed your number, {guess} correctly!!')
    print("")
    ComputerGuess(x)

# x = input(f'Insert the upper limit for guessing :')

ComputerGuess(1000)


