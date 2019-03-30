# File name: warmupDay6.py
number = int(input("Guess the secret number!"))
while number != 9:
    print("Try again")
    number = int(input("(Hint: It is a odd number) "))
print("You guessed right!")

lettern = int(input("Choose a value for n "))
letterm = int(input("Choose a value for m "))
print( lettern, " to the power of ", letterm, " is ", lettern**letterm )

guess = 10
while guess != -1:
    print(guess)
    guess -= 1