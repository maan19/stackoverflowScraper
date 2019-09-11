from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import operator
import collections

#query should not have spaces e.g data+science is a valid query
#returns top 10 hot skills for the query

def top_skills(query):
    skills = {}
    for x in range(1,5):
        if x==1:
            my_url = "https://stackoverflow.com/jobs?q=" + query
        else:
            my_url = "https://stackoverflow.com/jobs?q=" + query + 'sort=i&pg=' + str(x)
        
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html,"html.parser")
        tags = page_soup.findAll("a", {"class":"post-tag job-link no-tag-menu"})
        skill = ""

        for tag in tags:
            skill = tag.text
            if skill not in skills:
                skills[skill] = 1
            else:
                skills[skill]  = skills[skill] + 1

    sorted_skills = sorted(skills.items(), key=operator.itemgetter(1),reverse=True)
    top = []
    for i in range (0, 12):
        top.append(sorted_skills[i][0])
    
    return top






    





