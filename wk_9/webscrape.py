
# import bs4
from bs4 import BeautifulSoup
with open('webscrape.html', mode='r') as wf:
    #extract contents
    html = wf.read()
    # print(html)
    #parse to BeautifulSoup to webscrape
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    #finds values in html document
    prof_interests = soup.find(id="prof-int")
    #prints html attributes and text
    print(prof_interests)
    # prints text
    print(prof_interests.text)
    print(type(prof_interests))

    #navigate DOM tree
    personal_list = soup.find(id="pers_list")
    print(personal_list)
    print(personal_list.text)

    for c in personal_list.children:
        print(c)
        print(c.string)
