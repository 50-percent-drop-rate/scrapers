##Story 1: Saudi Arabia kills journalist, Jamal Khashoggi
##Story 2: Hurricane Michael
##Story 3: Legalization of marijuana in Canada


##using command line tool from https://github.com/taspinar/twitterscraper



#story1 
twitterscraper "Khashoggi" -o khashoggiall.csv -bd  "2018-09-16" -l 1500000 -p 25 -c


## story 2

twitterscraper "Hurricane AND Michael" -o michaelall.csv -bd  "2018-09-16" -l 2000000 -p 25 -c

#story3

twitterscraper "Canada AND Marijuana" -o weedall.csv -bd  "2018-09-16" -l 1000000 -p 25 -c