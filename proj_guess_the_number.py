import random

guess = input("Guess my number - it's between 0 and 20:")

def guess_filter(guess):
#This function gets the user's guess, and makes sure it is an integer between 0 and 20; if it's not then
#the function gives an error message and starts again
    
    if guess in map(str, range(0, 21, 1)):
        guess_assessor(guess)
    else:
        guess = input('Sorry, I need an integer value between 0 and 20...')
        guess_filter(guess)


def guess_assessor(guess):
#This function takes the user's guess and, if correct, tells the user so. If not correct, then tells the user
#so, and whether their guess was higher or lower than the correct answer. It also gives an updated range within
#which the answer lies, based on the user's prior guesses.
    
    global target
    global bounds

    guess = int(guess)
    if guess == target:
        print('Congratulations! ' + str(guess) + ' is correct.')
    else:
        if bounds['lower_bound'] <= guess < target:
            print("That's too low...")
            bounds['lower_bound'] = guess + 1
            guess = input("try again - my number is between " + str(bounds['lower_bound']) + " and "
                          + str(bounds['upper_bound']) + ":")
            guess_filter(guess)
            
        elif target < guess <= bounds['upper_bound']:
            print("That's too high...")
            bounds['upper_bound'] = guess - 1
            guess = input("try again - my number is between " + str(bounds['lower_bound']) + " and "
                          + str(bounds['upper_bound']) + ':')
            guess_filter(guess)

    
bounds = {'lower_bound' : 0, 'upper_bound' : 20}

target = random.randint(0, 20)

guess_filter(guess)





    
