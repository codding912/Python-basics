name = str(input('Please enter your name: '))
holder = 'Mamadou'
if name == holder:
    print('Bingo! ', name)
else:
     def printting():
        counter = 1
        while name != holder and counter < 3:
            guess = str(input('Please try again: '))
            counter += 1
        if guess == holder:
            print('Yes bingo ', guess)
        else:
            print('You reached the limit but nothing')

     printting()



