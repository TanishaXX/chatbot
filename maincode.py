#program assumes the requests are about the office when not talking about recommendations.
#can give option in beginning to talk about other show?
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


def whoquestions(q):

    '''function for who questions'''

    if ('main' in q or 'lead' in q) and ('characters' in q or 'character' in q):
        print("The main characters in The Office are: Michael Scott, Dwight Schrute, Pamela Beesly and Jim Halpert.")
    elif ('secondary' in q or 'smaller' in q) and ('characters' in q or 'character' in q):
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
    elif ('main' in q or 'lead' in q) and ('cast' in q or 'members' in q or 'actors' in q):
        print("The lead cast members of The Office are: Steve Carell(plays Michael Scott), John Krasinski(plays Jim halpert), Jenna Fischer(plays Pam Beesly) and Rainn Wilson(plays Dwight Schrute).")
    elif ('secondary' in q or 'smaller' in q) and ('cast' in q or 'members' in q or 'actors' in q):
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
    elif 'plays' in q or 'actor' in q:
        if 'Jim' in q or 'jim' in q:
            print("Jim Halpert is played by John Krasinski")
        elif 'Dwight' in q or 'dwight' in q:
            print("Dwight Schrute is played by Rainn Wilson")
        elif 'Michael' in q or 'michael' in q:
            print("Michael Scott is played by Steve Carell")
        elif 'Pam' in q or 'pam' in q:
            print("Pam Beesly is played by Jenna Fischer")
        elif 'Kevin' in q or 'kevin' in q:
            print("Kevin Malone is played by Brian Baumgartner")
        elif 'Angela' in q or 'angela' in q:
            print("Angela Martin is played by Angela Kinsey")
        elif 'Creed' in q or 'creed' in q:
            print("Creed Batton is played by Creed Batton")
        elif 'Oscar' in q or 'oscar' in q:
            print("Oscar Martinez is played by Oscar Nunez")
        elif 'Stanley' in q or 'stanley' in q:
            print("Stanley Hudson is played by Leslie David Baker")
        elif 'Ryan' in q or 'ryan' in q:
            print("Ryan Howard is played by BJ Novak")
        elif 'Kelly' in q or 'kelly' in q:
            print("Kelly Kapoor is played by Mindy Kaling")
        elif 'Toby' in q or 'toby' in q:
            print("Toby Flenderson is played by Paul Lieberstein")
        elif 'Phyllis' in q or 'phyllis' in q:
            print("Phyllis Vance is played by Phyllis Smith")
        elif 'Meredith' in q or 'meredith' in q:
            print("Meredith Palmer is played by Kate Flannery")
        elif 'Andy' in q or 'andy' in q:
            print("Andy Bernard is played by Ed Helms")

def whenquestions(q):

    ''' function for when questions'''

    if 'air' in q or 'release' in q or 'released' in q or 'aired' in q:
        if 'last' in q:
            print("The Office released its last episode on 16 May 2013. If this does not answer your question, please frame your request in a different way")
        elif 'pilot' in q or 'first' in q:
            print("The Office released its pilot on 24 March 2005. If this does not answer your question, please frame your request in a different way")
        else:
            print("The Office released its pilot on 24 March 2005. If this does not answer your question, please frame your request in a different way")
    if 'begin' in q or 'start' in q:
        print("The Office released its pilot on 24 March 2005. If this does not answer your question, please frame your request in a different way")
    elif 'end' in q or 'finish' in q:
        print("The Office released its last episode on 16 May 2013. If this does not answer your question, please frame your request in a different way")

def wherequestions(q):

    ''' function for where questions'''

    if 'watch' in q or 'stream' in q:
        print("The Office is available for streaming on Amazon Prime, Netflix, Peacock and Disney+")
    elif 'shot' in q or 'set' in q or 'filmed' in q:
        print('The office was mainly shot at Chandler Valley Centre Studios in Panorama City, California.')


def whichquestions(q):

    ''' function for which questions'''

    if 'platform' in q or 'OTT' in q or 'app' in q:
        print("The Office is available for streaming on Amazon Prime, Netflix, Peacock and Disney+")

def howquestions(q):

    ''' function for how questions'''

    if "seasons" in q and "many" in q:
        print("The Office has 9 seasons.")
    elif 'episodes' in q and 'many' in q:
        print("The Office has 201 episodes across 9 seasons.")





def info(): # function to enter when user wants information about the show

    '''function to enter when user wants information about the show'''

    print("Type in your request")
    thirdChoice = input()
    
    thirdChoice = list(thirdChoice.split(' '))  #converting the response into a list to parse through it

    if thirdChoice[0] == 'how' or thirdChoice[0] == 'How':
        howquestions(thirdChoice)
   
    elif thirdChoice[0] == 'when' or thirdChoice[0] == 'When':
        whenquestions(thirdChoice)

    elif thirdChoice[0] == 'who' or thirdChoice[0] == 'Who':
        whoquestions(thirdChoice)
          
    elif thirdChoice[0] == 'where' or thirdChoice[0] == 'Where':
        wherequestions(thirdChoice)

    elif thirdChoice[0] == 'which' or thirdChoice[0] == 'Which':
        whichquestions(thirdChoice)

def stats(): #function to enter when user wants statistics about the show

    print("Type in your request")
    thirdChoice = input()

def cast(): #function to enter when user wants to know about the cast of the show
    print("Type in your request")
    thirdChoice = input()

def funfacts(): 
    
    '''function to enter when user wants fun facts about the show'''
    
    print("Type in your request")
    thirdChoice = input()

def genreRecs():

    print('Would you like recommendations in comedy, action, crime, sci-fi, mystery or drama?')
    gChoice = input()
    gChoice = list(gChoice.split(' '))

    if 'comedy' in gChoice or 'Comedy' in gChoice:

        print('Would you like to choose a specific streaming service choice from Netflix, Amazon Prime or HBO Max? If so, please type in your choice')
        sChoice = list(input().split())

        if 'Netflix' in sChoice or 'netflix' in sChoice:
            shows = []
            while len(shows) < 5:
                t = random.randint(1, 12)

                webData = requests.get('https://www.tvguide.com/streaming/netflix/comedy/show/1/?sort=highestRated&network=netflix&genre=comedy&type=show&releaseYearMin=2000&releaseYearMax=2020&page={0}'.format(t))
                soup = BeautifulSoup(webData.content, 'html.parser')
                l = list(soup.find_all('h3', class_='g-text-xlarge g-text-bold g-outer-spacing-bottom-xsmall'))

                rc = random.choice(l).get_text().strip()
                if rc in shows:
                    continue
                shows.append(rc)

            inData = pd.DataFrame({'Comedy Recommendations': shows})

            inData.to_excel('tableData.xlsx', index=False)
            outData = pd.read_excel('tableData.xlsx', engine = 'openpyxl', index_col = None)

            print(outData)

        elif 'Prime' in sChoice or 'prime' in sChoice :
            shows = []

            while len(shows) < 5:

                t = random.randint(1, 7)
                webData = requests.get('https://www.tvguide.com/streaming/amazon-prime/comedy/show/1/?sort=highestRated&network=amazon-prime&genre=comedy&type=show&releaseYearMin=2000&releaseYearMax=2020&page={0}'.format(t))
                soup = BeautifulSoup(webData.content, 'html.parser')
                l = list(soup.find_all('h3', class_='g-text-xlarge g-text-bold g-outer-spacing-bottom-xsmall'))

                rc = random.choice(l).get_text().strip()
                if rc in shows:
                    continue
                shows.append(rc)

                inData = pd.DataFrame({'Comedy Recommendations': shows})

            inData.to_excel('tableData.xlsx', index=False)
            outData = pd.read_excel('tableData.xlsx', engine = 'openpyxl', index_col = None)

            print(outData)

        elif 'HBO' in sChoice or 'hbo' in sChoice or 'Hbo' in sChoice:
            shows = []
            while len(shows) < 5:
                t = random.randint(1, 8)

                webData = requests.get('https://www.tvguide.com/streaming/hbo-max/comedy/show/1/?sort=highestRated&network=hbo-max&genre=comedy&type=show&releaseYearMin=2000&releaseYearMax=2020&page={0}'.format(t))
                soup = BeautifulSoup(webData.content, 'html.parser')
                l = list(soup.find_all('h3', class_='g-text-xlarge g-text-bold g-outer-spacing-bottom-xsmall'))

                rc = random.choice(l).get_text().strip()
                if rc in shows:
                    continue
                shows.append(rc)

            inData = pd.DataFrame({'Comedy Recommendations': shows})

            inData.to_excel('tableData.xlsx', index=False)
            outData = pd.read_excel('tableData.xlsx', engine = 'openpyxl', index_col = None)

            print(outData)

        elif 'no' in sChoice or 'No' in sChoice:
            shows = []
            while len(shows) < 5:
                t = random.randint(1, 150)

                webData = requests.get('https://www.tvguide.com/streaming/all/comedy/show/1/?sort=highestRated&genre=comedy&type=show&releaseYearMin=2000&releaseYearMax=2020&page={0}'.format(t))
                soup = BeautifulSoup(webData.content, 'html.parser')
                l = list(soup.find_all('h3', class_='g-text-xlarge g-text-bold g-outer-spacing-bottom-xsmall'))

                rc = random.choice(l).get_text().strip()
                if rc in shows:
                    continue
                shows.append(rc)

            inData = pd.DataFrame({'Comedy Recommendations': shows})

            inData.to_excel('tableData.xlsx', index=False)
            outData = pd.read_excel('tableData.xlsx', engine = 'openpyxl', index_col = None)

            print(outData)

        else:
            print("Sorry, I don't understand what you meant. Please try again.")





print("Welcome to the Office bot. I am Dwight Schrute.")
print("I specialize in information of The Office but I can recommend other shows as well.")
print("What would you like to do?")
print("Would you like to talk about the show, get recommendations or get fun facts about the show?")

startChoice = input()

startChoice = list(startChoice.split(' '))

'''converting the response into a list to parse through it'''

for i in startChoice:
    if i == 'talk' or i == 'information':
        print("Would you like to get general information about the show, get statistics about the show, talk about the cast or get fun facts about the show?")
        secondChoice = input()
        break
    elif i == 'recommendations' or i == 'recommendation' or i == 'recs':
        print("Would you like to get recommendations according to genre, a cast member, or get popular tv shows?")
        secondChoice = input()
        break
    elif i == 'fun' or i == 'facts' or i == 'fun facts' or i == 'funfacts':
        funFacts()
        break


secondChoice = list(secondChoice.split(' '))  

'''converting the response into a list to parse through it'''

for i in secondChoice:
    if i == 'information'or i == 'info':
        info()
        break
    elif i == 'statistics'or i == 'stats':
        stats()
        break
    elif i == 'cast':
        cast()
        break
    elif i == 'fun' or i == 'facts' or i == 'fact':
        funfacts()
        break

    elif i == 'genre':
        genreRecs()
        break
    elif i == 'cast':
        castRecs()
        break