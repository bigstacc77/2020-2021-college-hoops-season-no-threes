from requests import get
from bs4 import BeautifulSoup

#url
url = 'https://www.espn.com/mens-college-basketball/teams'

#setup
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
thing = []
linkList = []
gameList = []

#gets team urls
for a in soup.findAll('a', {'tabindex':'0'}, class_ = 'AnchorLink'):
    test = a['href']
    test = test.replace('/mens-college-basketball', 'https://espn.com/mens-college-basketball')
    if 'espn.com/mens-college-basketball/team/_/id' in test:
        thing.append(test)

#remove duplicates
for i in thing:
    if i not in linkList:
        linkList.append(i)

#get game urls
for item in linkList:
    teamURL = item
    response2 = get(teamURL)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    type(soup2)
    for b in soup2.findAll('a', {'name':'&lpos=mens-college-basketball:teamclubhouse:schedule:regular'}, href=True):
        test2 = b['href']
        test2 = test2.replace('/mens-college-basketball/game?', 'espn.com/mens-college-basketball/matchup?')
        gameList.append(test2)

#calculate scores w/o threes using game urls
