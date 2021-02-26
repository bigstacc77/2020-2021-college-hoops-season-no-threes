#import stuff
from requests import get
from bs4 import BeautifulSoup

#url that you want to get results from
url = input("What game would you like to see? Make sure that it is from ESPN and on the 'Team Stats' page and not the 'Gamecast'.")

#literally just setup
sep = '-'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

#Lists the time left in the half or says that it's final
timeLeft = html_soup.find('span', class_ = 'status-detail')
print(timeLeft.next_element)

#Lists the home team's score
rightTeam = html_soup.find('div', class_ = 'score icon-font-before')
teamName = html_soup.find_all('span', class_ = 'long-name')
homeTeamName = teamName[1].next_element
print(homeTeamName + "'s score is " + str(rightTeam.next_element))

#Lists the away team's score
leftTeam = html_soup.find('div', class_ = 'score icon-font-after')
awayTeamName = teamName[0].next_element
print(awayTeamName + "'s score is " + str(leftTeam.next_element))

#Finds three pointers for both teams
table = html_soup.findAll('table')
threeptTest = table[1]
threeptTest2 = threeptTest.find_all('tr', {"data-stat-attr":"threePointFieldGoalsMade-threePointFieldGoalsAttempted"})
threeptTest3 = threeptTest2[0]
threeptTest4 = threeptTest3.find_all('td')

#Lists the away team's three pointers
leftTeamThrees = threeptTest4[1].next_element
leftTeamThrees = leftTeamThrees.replace('\n', '')
leftTeamThrees = leftTeamThrees.replace('\t', '')
leftTeamThrees = leftTeamThrees.split(sep, 1)[0]
print(awayTeamName + "'s made " + str(leftTeamThrees) + " three pointers this game")

#Lists the home team's three pointers
rightTeamThrees = threeptTest4[2].next_element
rightTeamThrees = rightTeamThrees.replace('\n', '')
rightTeamThrees = rightTeamThrees.replace('\t', '')
rightTeamThrees = rightTeamThrees.split(sep, 1)[0]
print(homeTeamName + "'s made " + str(rightTeamThrees) + " three pointers this game")

#Calculates adjusted scores
leftTeamAdjust = int(leftTeam.next_element) - int(leftTeamThrees)
rightTeamAdjust = int(rightTeam.next_element) - int(rightTeamThrees)

#Lists adjusted scores
print(homeTeamName + "'s adjusted score is " + str(rightTeamAdjust))
print(awayTeamName + "'s adjusted score is " + str(leftTeamAdjust))
