from dotenv import load_dotenv
import os
import json
from newsapi import NewsApiClient

##Story 1: Saudi Arabia kills journalist, Jamal Khashoggi
##Story 2: Hurricane Michael
##Story 3: Legalization of marijuana in Canada
load_dotenv()
APIKEY = os.getenv("APIKEY")

newapi = NewsApiClient(api_key = APIKEY)

runStoryOne = True
runStoryTwo = True
runStoryThree = True

story1Contents = []
story1Keywords = "Kashoggi AND Saudi Arabia"

story2Contents = []
story2Keywords = "Hurricane Michael"

story3Contents = []
story3Keywords = "Canada AND Marijuana"

if(runStoryOne):
    count = 0
    totalResults = 1
    while count < totalResults/4: ##We want the top 25% of results
        story1 = newapi.get_everything(q = story1Keywords, language = "en",  page_size = 100, sort_by="popularity")
        for story in story1["articles"]:
            story1Contents.append(story)
        totalResults = story1["totalResults"]
    with open('story1.json', 'w') as outfile:  
        json.dump(story1Contents, outfile) 

if(runStoryTwo):
    count = 0
    totalResults = 1
    while count < totalResults/4:
        story2 = newapi.get_everything(q = story2Keywords, language = "en",  page_size = 100, sort_by="popularity")
        for story in story2["articles"]:
            story2Contents.append(story)
        totalResults = story2["totalResults"]
    with open('story2.json', 'w') as outfile:  
        json.dump(story2Contents, outfile)

if(runStoryThree):
    count = 0
    totalResults = 1
    while count < totalResults/4:
        story3 = newapi.get_everything(q = story3Keywords, language = "en",  page_size = 100, sort_by="popularity")
        for story in story3["articles"]:
            story3Contents.append(story)
        totalResults = story3["totalResults"]
    with open('story3.json', 'w') as outfile:  
       json.dump(story3Contents, outfile) 