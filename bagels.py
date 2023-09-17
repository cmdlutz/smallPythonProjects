import sys
import random


print('\n\nBagels - A Deductive Logic Game')
print('Try to Guess the N-Digit Number I am thinking.\n')
print('''When I Say:        That means:
            Pico                One digit is correct but in the wrong position.
            Fermi               One digit is correct and in the right position.
            Bagels              Nothing is correct.
\n''')


def generateNumber(sigfigs):
    baseOptions = '0123456789'
    #copy the baseOptions N number of times into list
    baseOptList = list(baseOptions*sigfigs)
    #shuffle list
    random.shuffle(baseOptList)
    #grab req number of sigfigs
    resultStr = ''.join(baseOptList[:sigfigs])
    #return result
    #print('My Number is', resultStr)
    print('I have my number. It is', sigfigs, 'characters long.')
    return resultStr


def checkGuess(guess, answer):
    rslt = []
    for i in range(0, len(answer)):
        if guess[i] == answer[i]:
            rslt.append('fermi')
        elif guess[i] in answer:
            rslt.append('pico')
    if len(rslt) == 0:
        print('Bagels')
    else:
        rslt.sort()
        print( ' '.join(rslt) )


def main():
    try:
        #game loop
        while(True):
            #user setup
            answerLen = int(input('Please enter the amount of numbers you would like in the game \n'))
            numberOfGuesses = int(input('Please enter the amount of guesses you would like to have \n'))
            #generate new number
            MyNumber = generateNumber(answerLen)
            #main loop
            for i in range(1, numberOfGuesses+1):
                print('Your Guess Number', i, "is:")
                userGuess = input()
                #Correct/Wrong Answer
                if userGuess == MyNumber:
                    print('You Got it!')
                    break
                elif len(userGuess) == answerLen:
                    checkGuess(userGuess, MyNumber)
                else:
                    print('Guess Appears to be the wrong length. Try again.')
            #restart or exit
            restart = input('GAME OVER. Answer was {} Would you like to try again? (y) to continue. \n'.format(MyNumber))
            if restart in ('y','Y'):
                pass
            else:
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        print('Goodbye')
        sys.exit()


if __name__ == "__main__":
    main()
