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


##story 1 by weeks
twitterscraper "Khashoggi" -o khashoggi916.csv -bd  "2018-09-16" -l 500000 -ed "2018-09-22" -c
twitterscraper "Khashoggi" -o khashoggi923.csv -bd  "2018-09-23" -l 500000 -ed "2018-09-29" -c
twitterscraper "Khashoggi" -o khashoggi930.csv -bd  "2018-09-30" -l 500000 -ed "2018-10-06" -c
twitterscraper "Khashoggi" -o khashoggi1007.csv -bd  "2018-10-07" -l 500000 -ed "2018-10-13" -c
twitterscraper "Khashoggi" -o khashoggi1014.csv -bd  "2018-10-14" -l 500000 -ed "2018-10-20" -c
twitterscraper "Khashoggi" -o khashoggi1021.csv -bd  "2018-10-21" -l 500000 -ed "2018-10-27" -c
twitterscraper "Khashoggi" -o khashoggi1028.csv -bd  "2018-10-28" -l 500000 -ed "2018-11-03" -c

##story 2 by weeks
twitterscraper "Hurricane AND Michael" -o michael916.csv -bd  "2018-09-16" -l 500000 -ed "2018-09-22" -c
twitterscraper "Hurricane AND Michael" -o michael923.csv -bd  "2018-09-23" -l 500000 -ed "2018-09-29" -c
twitterscraper "Hurricane AND Michael" -o michael930.csv -bd  "2018-09-30" -l 500000 -ed "2018-10-06" -c
twitterscraper "Hurricane AND Michael" -o michael1007.csv -bd  "2018-10-07" -l 500000 -ed "2018-10-13" -c
twitterscraper "Hurricane AND Michael" -o michael1014.csv -bd  "2018-10-14" -l 500000 -ed "2018-10-20" -c
twitterscraper "Hurricane AND Michael" -o michael1021.csv -bd  "2018-10-21" -l 500000 -ed "2018-10-27" -c
twitterscraper "Hurricane AND Michael" -o michael1028.csv -bd  "2018-10-28" -l 500000 -ed "2018-11-03" -c

##story 3 by weeks
twitterscraper "Canada AND Marijuana" -o weed916.csv -bd  "2018-09-16" -l 500000 -ed "2018-09-22" -c
twitterscraper "Canada AND Marijuana" -o weed923.csv -bd  "2018-09-23" -l 500000 -ed "2018-09-29" -c
twitterscraper "Canada AND Marijuana" -o weed930.csv -bd  "2018-09-30" -l 500000 -ed "2018-10-06" -c
twitterscraper "Canada AND Marijuana" -o weed1007.csv -bd  "2018-10-07" -l 500000 -ed "2018-10-13" -c
twitterscraper "Canada AND Marijuana" -o weed1014.csv -bd  "2018-10-14" -l 500000 -ed "2018-10-20" -c
twitterscraper "Canada AND Marijuana" -o weed1021.csv -bd  "2018-10-21" -l 500000 -ed "2018-10-27" -c
twitterscraper "Canada AND Marijuana" -o weed1028.csv -bd  "2018-10-28" -l 500000 -ed "2018-11-03" -c