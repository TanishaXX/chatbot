#program assumes the requests are about the office when not talking about recommendations.
#can give option in beginning to talk about other show?

def whoquestions(l3):

    '''function for who questions'''

    if ('main' in l3 or 'lead' in l3) and ('characters' in l3 or 'character' in l3):
        print("The main characters in The Office are: Michael Scott, Dwight Schrute, Pamela Beesly and Jim Halpert.")
    elif ('secondary' in l3 or 'smaller' in l3) and ('characters' in l3 or 'character' in l3):
        print("The secondary charcters in The Office are:")
        print("Angela Martin")
        print("Creed Batton")
        print("Kevin Malone")
        print("Oscar Martinez")
        print("Stanley Hudson")
        print("Ryan Howard")
        print("Kelly Kapoor")
        print("Toby Flenderson")
        print("Phyllis Vance")
        print("Meredith Palmer")
        print("Andy Bernard")
    elif ('main' in l3 or 'lead' in l3) and ('cast' in l3 or 'members' in l3 or 'actors' in l3):
        print("The lead cast members of The Office are: Steve Carell(plays Michael Scott), John Krasinski(plays Jim halpert), Jenna Fischer(plays Pam Beesly) and Rainn Wilson(plays Dwight Schrute).")
    elif ('secondary' in l3 or 'smaller' in l3) and ('cast' in l3 or 'members' in l3 or 'actors' in l3):
        print("The secondary cast members in The Office are:")
        print("Angela Kinsey(plays Angela Martin)")
        print("Creed Batton(plays Creed Batton)")
        print("Brian Baumgartner(plays Kevin Malone)")
        print("Oscar Nunez(plays Oscar Martinez)")
        print("Leslie David Baker(plays Stanley Hudson)")
        print("BJ Novak(plays Ryan Howard)")
        print("Mindy Kaling(plays Kelly Kapoor)")
        print("Paul Lieberstein(plays Toby Flenderson)")
        print("Phyllis Smith(plays Phyllis Vance)")
        print("Kate Flannery(plays Meredith Palmer)")
        print("Ed Helms(plays Andy Bernard)")
    elif 'plays' in l3 or 'actor' in l3:
        if 'Jim' in l3 or 'jim' in l3:
            print("Jim Halpert is played by John Krasinski")
        elif 'Dwight' in l3 or 'dwight' in l3:
            print("Dwight Schrute is played by Rainn Wilson")
        elif 'Michael' in l3 or 'michael' in l3:
            print("Michael Scott is played by Steve Carell")
        elif 'Pam' in l3 or 'pam' in l3:
            print("Pam Beesly is played by Jenna Fischer")
        elif 'Kevin' in l3 or 'kevin' in l3:
            print("Kevin Malone is played by Brian Baumgartner")
        elif 'Angela' in l3 or 'angela' in l3:
            print("Angela Martin is played by Angela Kinsey")
        elif 'Creed' in l3 or 'creed' in l3:
            print("Creed Batton is played by Creed Batton")
        elif 'Oscar' in l3 or 'oscar' in l3:
            print("Oscar Martinez is played by Oscar Nunez")
        elif 'Stanley' in l3 or 'stanley' in l3:
            print("Stanley Hudson is played by Leslie David Baker")
        elif 'Ryan' in l3 or 'ryan' in l3:
            print("Ryan Howard is played by BJ Novak")
        elif 'Kelly' in l3 or 'kelly' in l3:
            print("Kelly Kapoor is played by Mindy Kaling")
        elif 'Toby' in l3 or 'toby' in l3:
            print("Toby Flenderson is played by Paul Lieberstein")
        elif 'Phyllis' in l3 or 'phyllis' in l3:
            print("Phyllis Vance is played by Phyllis Smith")
        elif 'Meredith' in l3 or 'meredith' in l3:
            print("Meredith Palmer is played by Kate Flannery")
        elif 'Andy' in l3 or 'andy' in l3:
            print("Andy Bernard is played by Ed Helms")

def whenquestions(l3):

    ''' function for when questions'''

    if 'air' in l3 or 'release' in l3 or 'released' in l3 or 'aired' in l3:
        if 'last' in l3:
            print("The Office released its last episode on 16 May 2013. If this does not answer your question, please frame your request in a different way")
        elif 'pilot' in l3 or 'first' in l3:
            print("The Office released its pilot on 24 March 2005. If this does not answer your question, please frame your request in a different way")
    if 'begin' in l3 or 'start' in l3:
        print("The Office released its pilot on 24 March 2005. If this does not answer your question, please frame your request in a different way")
    elif 'end' in l3 or 'finish' in l3:
        print("The Office released its last episode on 16 May 2013. If this does not answer your question, please frame your request in a different way")

def wherequestions(l3):

    ''' function for where questions'''

    if 'watch' in l3 or 'stream' in l3:
        print("The Office is available for streaming on Amazon Prime, Netflix, Peacock and Disney+")

def whichquestions(l3):

    ''' function for which questions'''

    if 'platform' in l3 or 'OTT' in l3 or 'app' in l3:
        print("The Office is available for streaming on Amazon Prime, Netflix, Peacock and Disney+")

def howquestions(l3):

    ''' function for how questions'''

    if "seasons" in l3 and "many" in l3:
        print("The Office has 9 seasons.")
    elif 'episodes' in l3 and 'many' in l3:
        print("The Office has 201 episodes across 9 seasons.")




def info(): # function to enter when user wants information about the show

    '''function to enter when user wants information about the show'''

    print("Type in your request")
    thirdChoice = input()
    
    l3 = thirdChoice.split(' ')  #converting the response into a list to parse through it

    if l3[0] == 'how' or l3[0] == 'How':
        howquestions(l3)
   
    elif l3[0] == 'when' or l3[0] == 'When':
        whenquestions(l3)

    elif l3[0] == 'who' or l3[0] == 'Who':
        whoquestions(l3)
          
    elif l3[0] == 'where' or l3[0] == 'Where':
        wherequestions(l3)

    elif l3[0] == 'which' or l3[0] == 'Which':
        whichquestions(l3)

def stats(): #function to enter when user wants statistics about the show

    print("Type in your request")
    thirdChoice = input()

def cast(): #function to enter when user wants to know about the cast of the show
    print("Type in your request")
    thirdChoice = input()

def funfacts(): #function to enter when user wants fun facts about the show
    print("Type in your request")
    thirdChoice = input()


print("Welcome to the Office bot. I am Dwight Schrute.")
print("I specialize in information of The Office but I can recommend other shows as well.")
print("What would you like to do?")
print("Would you like to talk about the show, get recommendations or watch moments from a show?")

startChoice = input()

l1 = startChoice.split(' ') #converting the response into a list to parse through it

for i in l1:
    if i == 'talk' or i == 'information':
        print("Would you like to get information about the show, get statistics about the show, talk about the cast or get fun facts about the show?")
        secondChoice = input()
        break
    elif i == 'recommendations' or i == 'recommendation':
        print("Would you like to get recommendtions according to genre, a cast member or creator?")
        secondChoice = input()
        break
    elif i == 'moments' or  i == 'clips' or i == 'watch':
        print("Which moment would you like to see?")
        secondChoice = input()
        break


l2 = secondChoice.split(' ')  #converting the response into a list to parse through it

for i in l2:
    if i == 'information':
        info()
        break
    elif i == 'statistics':
        stats()
        break
    elif i == 'cast':
        cast()
        break
    elif i == 'fun':
        funfacts()
        break
    