#User inputs text and rick astley cipher is returned.
#rick astley chipher encoder
#moongazer07

def encodeUserMsg(userInput):
    msg = ""
    RICKbet = {
                'A' : "NEVER ",
                'B' : "GONNA ",
                'C' : "GIVE ",
                'D' : "YOU ",
                'E' : "UP ",
                'F' : "Never ",
                'G' : "Gonna ",
                'H' : "LET ",
                'I' : "You ",
                'J' : "DOWN ",
                'K' : "NEver ",
                'L' : "GOnna ",
                'M' : "TURN ",
                'N' : "AROUND ",
                'O' : "AND ",
                'P' : "DESERT ",
                'Q' : "YOu ",
                'R' : "NEVer ",
                'S' : "gonna ",
                'T' : "TELL ",
                'U' : "A ",
                'V' : "LIE ",
                'W' : "and ",
                'X' : "HURT ",
                'Y' : "you ",
                'Z' : "rick astley ",
                ' ' : "+ "
                }
    for ittr in range(len(userInput)):
        if(userInput[ittr].isalpha() or userInput[ittr] == ' '):
            msg += (RICKbet[userInput[ittr]])
    print(msg+"\n=")



print('rick cipher')
userInput = input("Please enter text to protect: ")
encodeUserMsg(userInput.upper())

while True:
    userInput = input("Would you like to continue? press Enter without typing anything to quit or type text and press enter to continue: ")
    if (userInput == ''):
        break
    encodeUserMsg(userInput.upper())
