# 2020-2021-college-hoops-season-no-threes
Work-in-progress script that gathers every played game (that has team stats available on ESPN) of the 2020-21 college basketball season, gets the number of three pointers from the game, calculates the score of said game without threes, then writes it all to a .csv file you can import into a spreadsheet.

At the moment, this only takes into account the number of three pointers and doesn't remove any duplicates from the final list. Takes a while to finish running, mainly because it takes a long time to do calculations for every single game (there are 350+ Division 1 teams with each of them playing 20+ games). Planning to improve this script further by adding a list of games that went to OT for manual review (since no stats exist for threes during each half/OT), removing a third free throw from a shooting foul that occured outside of the three-point line, etc.

NOTE: This does NOT work with NBA games (except for the individual game program). Make sure that any individual games are on the "Team Stats" page instead of the default "Gamecast" page. Otherwise, the program does not work. For the individual team program, make sure that your team is on the overview section and not the "schedule" section.

# Requirements
To run this script, you will need Python 3.9.x, and the libraries listed in requirements.txt.
