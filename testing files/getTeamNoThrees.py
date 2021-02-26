from requests import get
from bs4 import BeautifulSoup
import csv

#url
url = input('What team would you like to remove threes from all games? Paste a url of the team.')

#setup
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)
gameList = []

#testing (please please please work)
for a in soup.findAll('a', {'name':'&lpos=mens-college-basketball:teamclubhouse:schedule:regular'}, href=True):
    test = a['href']
    test = test.replace('/mens-college-basketball/game?', 'https://espn.com/mens-college-basketball/matchup?')
    gameList.append(test)

#testing again
with open('collegehoops.csv', 'w', newline='') as f:
    hoops = csv.writer(f)
    hoops.writerow(['team 1', 'team 2', 'original team 1 score', 'original team 2 score', 'team 1 threes', 'team 2 threes', 'adjusted team 1 score', 'adjusted team 2 score'])
    for component in gameList:
        gameURL = component
        response2 = get(gameURL)
        html_soup = BeautifulSoup(response2.text, 'html.parser')
        sep = '-'
        
        #Checks to see if team stats are available
        teamStatCheck = html_soup.find('div', {'id':"gamepackage-matchup"}, {'data-module':'matchup'})
        if teamStatCheck is None:
            continue
        else:
            pass
        teamStatCheck = str(teamStatCheck.next_element)
        teamStatCheck = teamStatCheck.replace('\n', '')
        teamStatCheck = teamStatCheck.replace('\t', '')
        if teamStatCheck == 'No Team Stats Available':
            continue
        else:
            pass
        
        #Lists the time left in the half or says that it's final
        timeLeft = html_soup.find('span', class_ = 'status-detail')

        #Lists the home team's score
        rightTeam = html_soup.find('div', class_ = 'score icon-font-before')
        teamName = html_soup.find_all('span', class_ = 'long-name')
        homeTeamName = teamName[1].next_element
        rightTeam = str(rightTeam)

        if rightTeam == '<div class="score icon-font-before"></div>':
            continue
        else:
            pass
        
        #Lists the away team's score
        leftTeam = html_soup.find('div', class_ = 'score icon-font-after')
        awayTeamName = teamName[0].next_element

        #Finds three pointers for both teams
        table = html_soup.findAll('table')
        threeptTest = table[1]
        threeptTest2 = threeptTest.find_all('tr', {"data-stat-attr":"threePointFieldGoalsMade-threePointFieldGoalsAttempted"})
        threeptTest3 = threeptTest2[0]
        threeptTest4 = threeptTest3.find_all('td')

        #Cleans up three pointer string (away)
        leftTeamThrees = threeptTest4[1].next_element
        leftTeamThrees = leftTeamThrees.replace('\n', '')
        leftTeamThrees = leftTeamThrees.replace('\t', '')
        leftTeamThrees = leftTeamThrees.split(sep, 1)[0]
        
        #Cleans up three pointer string (home)
        rightTeamThrees = threeptTest4[2].next_element
        rightTeamThrees = rightTeamThrees.replace('\n', '')
        rightTeamThrees = rightTeamThrees.replace('\t', '')
        rightTeamThrees = rightTeamThrees.split(sep, 1)[0]

        #String cleanup
        rightTeam = rightTeam.replace('<div class="score icon-font-before">', '')
        rightTeam = rightTeam.replace('</div>', '')

        #Calculates adjusted scores
        leftTeamAdjust = int(leftTeam.next_element) - int(leftTeamThrees)
        rightTeamAdjust = int(rightTeam) - int(rightTeamThrees)

        #adds to csv file
        hoops.writerow([awayTeamName, homeTeamName, leftTeam.next_element, rightTeam, leftTeamThrees, rightTeamThrees, leftTeamAdjust, rightTeamAdjust])
