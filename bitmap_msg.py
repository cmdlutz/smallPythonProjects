import sys
import math
"""
    map user message to bitmap image
"""


def main():
    bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""
    print('Enter the message you wish to display.')
    msg = input()
    if msg == '' or msg.isspace():
        print('Nothing entered. Goodbye.')
        sys.exit()
    else:
        #step through bitmap
        for line in bitmap.splitlines():
            #step through bitmap lines
            for i in range(len(line)):
                length = len(msg)
                #update img
                if line[i] == '*':
                    print(msg[i % length], end='')
                elif line[i] == ' ':
                    print(' ', end='')
                elif line[i] == '.':
                    print('.', end='')
            #enter after each line
            print()


if __name__ == "__main__":
    main()
