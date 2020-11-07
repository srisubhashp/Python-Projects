import requests
from bs4 import BeautifulSoup
import pprint

res=requests.get('https://news.ycombinator.com/')
print(res.text)
soup=BeautifulSoup(res.text,'html.parser')
#print(soup.body)
#print(soup.body.contents)
#print(soup.find_all('div'))

#print(soup.find('p')) # only returns the first element found.

#print(soup.find(class="itemList"))

#print(soup.select('a')) # returns all the links of the webpage.
#print(soup.select('.score'))

links=soup.select('.storylink') # grabs everything with the class name of story link

#print(soup.select('.storylink')[1])


subText=soup.select('.subtext')

def sort_Stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes']) #syntax for arranging the code in ascending order

def create_custom_hn(links, subtext):
    hn=[]
    for idx, item in enumerate(links):
        title=links[idx].getText()
        href=links[idx].get('href',None)
        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title,'link':href,'votes':points})
    return sort_Stories_by_votes(hn)

#print(create_custom_hn(links,subText))
pprint.pprint(create_custom_hn(links,subText))



