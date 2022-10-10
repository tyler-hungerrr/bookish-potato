import random
def input_num(number): #validating the input as a number
    try:
        number = int(number)
    except ZeroDivisionError as err:
        print(err)
    except NameError as err:
        print(err)
    except ValueError as err:
        print(err)
    except KeyboardInterrupt as err:
        print(err)
    except Exception as err:
        print(err)
    return number

top_of_range = input("Type a number: ") #getting number from user

input_num(top_of_range)
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()

random_num = (random.randrange(0, top_of_range)) #generates a number

guesses = 0
while True: #loop where player guesses the number
    guesses += 1
    player_guess = input("Make a guess ")
    input_num(player_guess)
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        player_guess = int(player_guess)
        continue

    if player_guess == random_num:
        print("You got the right number!")
        break
    elif player_guess < random_num:
        print("You were below the random number.")
    else:
        print("You were above the random number.")

print("You got it in", guesses, "guesses")