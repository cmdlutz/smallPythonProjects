import datetime, random, re


"""
    Simulation for the birthday paradox    
"""


print('\n\nBirthday Paradox\n\n')


#generate desired number of birthdays
def generateBirthdays(amount):
    birthdays = []
    for i in range(amount+1):
        print(i)


def main():
    try:
        numBirthdays = input('How many birthdays would you like to generate? (Min:2 Max:100)\n')
        #check if only numbers
        if numBirthdays.isdigit() == False:
            print('No text please.')
        #check if in range
        elif int(numBirthdays) in range(2,101):
            birthdays = generateBirthdays(int(numBirthdays))
        #Else
        else:
            print('Out of range. Please try again.')
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == "__main__":
    main()
