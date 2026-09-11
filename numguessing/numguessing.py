import random 

randomnum = random.randint(1,100)
attempts = 0
guessnum = 0

high = 100
low = 1
    
while guessnum != randomnum:
    try:
        guessnum = int(input(f"Guess a number between {low} and {high}:\n"))
    except ValueError:
        print("Please enter only number, not letters or symbols")
        continue   
        # ignore all operations below and go back to the start of the loop, prompt for input back
    
    attempts += 1
    if guessnum < randomnum:
        low = guessnum + 1
        print("Your guess is lower than the actual number, try again")
    elif guessnum > randomnum:
        high = guessnum - 1
        print("Your guess is higher than the actual number, try again")
    else:
        break

print(f"Congrats, you guess the number {randomnum} in {attempts} attempts")



