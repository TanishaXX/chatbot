#program assumes the requests are about the office when not talking about recommendations.
#can give option in beginning to talk about other show?



def info(): #function to enter when user wants information about the show
    print("Type in your request")
    thirdChoice = input()
    l3 = thirdChoice.split(' ')

    if l3[0] == 'how' or l3[0] == 'How':
        if "seasons" and "many" and ("office" or "Office") in l3:
            print("The Office has 9 seasons. If this does not answer your question, please frame your request in a different way")
    elif l3[0] == 'when' or l3[0] == 'When':
        if ('last' and 'released' or 'aired' or 'air' or 'release') or 'finish':
            print("The Office released its last episode on 16 May 2013. If this does not answer your question, please frame your request in a different way")
        if 'air' or 'released' or 'aired' or 'start' or 'first' in l3:
            print("The Office released its pilot on 24 March 2005. If this does not answer your question, please frame your request in a different way")




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


l2 = secondChoice.split(' ')

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
    