num1 = int(input('Please enter a number '))
num2 = int(input('Please enter another number '))
result = num1 + num2
print(result)

# this is how to make functions in python
def sa_hi(name, age):
    print('Hello ' + name + ' you are ', int(age))
sa_hi('Mamadou', 34)


def cube(num):
    return num*num
print('Here is double of the number', cube(3))


def max_num():
    num3=int(input('Please enter a number '))
    num4=int(input('Please enter a number '))
    if num3 > num4:
        return num3
    else:
        return num4
print('The max is ' ,  max_num())


i=1
while i <= 10:
    i += 1
    print(i)
print(' I am done with loop')


#This is how to make and control a user try
secret_word = 'Mamadou'
guess = ''
count = 0
limit = 3
out_of_limit = False

while guess != secret_word and not(out_of_limit):
    if count < limit:
        guess = str(input('Please guess: '))
        count += 1
    else:
        out_of_limit = True

if out_of_limit:
    print('You lost the gane Dude!')
else:
    print('You won Boy!')


#This is how to make an expo fonction
def raise_pow(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result
print(raise_pow(2, 3))


#This is how to make nested loop to print lists
numbers = [
    [1, 2, 3],
    [3, 4, 5]
]

for row in numbers:
    for col in row:
        print(col)


#This is how toconverst voels in an input from users
def convertor():
    words = str(input('Please  words: '))
    convert = ''

    for letter in words:
        if letter.lower() in 'aeiou':

            if letter.isupper():
               convert = convert + 'G'
            else:
                convert = convert + 'g'

        else:
            convert = convert + letter
    return convert

print(convertor())


#This is how to handle exceptions try except
try:
    answer = 10/0
    number = int(input('Please enter a number: '))
    print(number)
except ValueError as err:
    print(err, 'Please read the prompt! ')
except ZeroDivisionError as err:
    print(err)



#This is how to read files in python
code_file = open('rtr.html', 'r') # r means write
#print(code_file.readable())  This line here is to check if the file is readable
for code in code_file.readlines():
    print(code)
code_file.close()


#This is how to create, write a file and add something inside the file
employee_files = open('Intern_2002.txt', 'a') # a means append that we can add something inside the file. W create and write
#employee_files.writable()
Intern =  str(input('Please enter the Intern name and position: '))
employee_files.write('\n'+ Intern)

employee_files.write('\nAlhassane Koney DataStructure ')

employee_files.close()


#This is how to make classes and import them in a different files
#one where the class in exported
from Student import Student

student1 = Student('Mamadou', 'CIS', 3.7, 'NYU')
student2 = Student('Diallo', 'CIS', 3.709, 'SPS')

print(student1.name)

#second file where the calss in created
class Student:

    def __init__(self, name, major, gpa, school):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.school = school



#This is how to make a game choice with classes
from Game import Questions

options = [
    'Where is NY?\n(a) USA\n(b) EUP\n(c) AFQ\n',
    'Where is FR?\n(a) USA\n(b) EUP\n(c) AFQ\n',
    'Where is GN?\n(a) USA\n(b) EUP\n(c) AFQ\n'
]

questions = [
    Questions(options[0], 'a'),
    Questions(options[1], 'b'),
    Questions(options[2], 'c'),
]


def go_play(questions):
    score = 0
    for choice in questions:
        answer = input(choice.prompt)
        if answer == choice.answer:
           score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct!')

go_play(questions)



#This function also combine with the Student function we can have honor roll
from Student import Student

student1 =  Student('Mamadou', 'CIS', 3.7, 'NYU')
student2 =  Student('Naoumy', 'CIS', 3.1, 'NYU')


print(student2.on_honor_roll())

class Student:

    def __init__(self, name, major, gpa, school):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.school = school

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False



#This is inheritance
class Cooker:
    def make_chikien(self):
        print('Cooker can make good chikiens')

    def make_salad(self):
        print('This restaurant can make good salads')

    def make_fruits(self):
        print('This Dude can bring good fruits')


from Chef import Cooker

class Uique(Cooker):

    def african_food(self):
        print('Rice and cousssousse')

from Chef import Cooker
from UnqChef import Uique

MyCooker = Cooker()
MyCooker.make_chikien()

AfrcanDish = Uique()
AfrcanDish.african_food()
AfrcanDish.make_salad()



#This is how to make a form where to ask and controle the the input for matches
def System():
    password = 'Diallo'
    count = 0
    limit = 3
    tryy = str(input('Please enter a password: '))

    while tryy != password and count <= limit:
        tryy = str(input('Please try again: '))
        count += 1

    if tryy == password:
        print('Bingo! ')
    else:
        print('Dude you reached the limit come back in 30 minutes! ')


System()