import datetime, random, re


"""
    Simulation for the birthday paradox    
"""


print('\n\nBirthday Paradox\n\n')


#generate desired number of birthdays
def generateBirthdays(amount):
    start_date = datetime.date(2000, 1, 1)
    birthdays = []
    for i in range(amount):
        #generate birthdays
        randomNumberOfDays = datetime.timedelta(random.randint(0,365))
        birthday = start_date + randomNumberOfDays
        #format
        formattedBirthday = birthday.strftime("%B %d, %Y")
        #add to list
        birthdays.append(formattedBirthday)
    return birthdays


#Check for matching birthdays
def getMatch(birthdays):
    isMatch = []
    break_out_flag = False
    for i in range(len(birthdays)):
        #set birthday to compare
        currentBD = birthdays[i]
        #see if there is a match in rest of birthdays
        for j in range(i+1,len(birthdays)):
            compareBD = birthdays[j]
            #terminate loop if match found
            if currentBD == compareBD:
                isMatch.append(currentBD)
                break_out_flag = True
                break
        if break_out_flag:
            break
    return isMatch


#Run simulation x number of times and return results as list
def runSimulation(timesToRun, numBirthdays):
    posTests = []
    for i in range(int(timesToRun)):
        birthdays = generateBirthdays(int(numBirthdays))
        match = getMatch(birthdays)
        #check if a match
        if len(match) > 0:
            posTests.append(match)
            #print('In this simulation, multiple people share a birthday on', match[0], '\n')
        else:
            #print('In this simulation, no matches were found \n')
            pass
    return posTests


def main():
    try:
        numBirthdays = input('How many birthdays would you like to generate? (Min:2 Max:100)\n')
        #check if only numbers
        if numBirthdays.isdigit() == False:
            print('No text please.')
        #check if in range
        elif int(numBirthdays) in range(2,101):
            birthdays = generateBirthdays(int(numBirthdays))
            print('\nHere are your requested birthdays:\n', birthdays, '\n')
            match = getMatch(birthdays)
            #check if a match
            if len(match) > 0:
                print('In this simulation, multiple people share a birthday on', match[0], '\n')
            else:
                print('In this simulation, no matches were found \n')
        #Else
        else:
            print('\nOut of range. Please try again.')

        #Ask for number of tests to run
        numSimulations = input('How many times would you like to run the test? (Min:2 Max:10,000)\n')
        if numSimulations.isdigit() == False:
            print('\nNo text please.')
        #Run Simulation
        elif int(numSimulations) in range(2, 10001):
            print('\nGenerating', numBirthdays, 'random birthdays', numSimulations, 'times \n')
            simResults = runSimulation(numSimulations, numBirthdays)
            print('Out of', numSimulations, 'simulations of', numBirthdays, 'people, there was a matching birthday in that group', len(simResults), 
                  'times. \nThis means that there is a', round(len(simResults)/int(numSimulations)*100, 2), '% chance of having a matching birthday in their group.\n')
        #Else
        else:
            print('\nOut of range. Please try again.')
    except KeyboardInterrupt:
        print('Goodbye')

if __name__ == "__main__":
    main()
