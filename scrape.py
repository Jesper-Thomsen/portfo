import requests
from bs4 import BeautifulSoup
import pprint


def getlinks(pages):
    links=[]
    subtext=[]
    for num in range(pages):
        link= 'https://news.ycombinator.com/news?p='+str(num)
        res=requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        links=links+soup.select('.titleline')
        subtext=subtext+soup.select('.subtext')
    return links, subtext



def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn=[]
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.find('a').get("href")
        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'Title': title, 'Link': href, 'votes': points})
    return sort_stories_by_votes(hn)

def print_results(pages):
    pprint.pprint(create_custom_hn(getlinks(pages)[0], getlinks(pages)[1]))

def make_html_friendly(sorted_dictionary_of_headlines):
    string_containing_links = []
    for items in sorted_dictionary_of_headlines:
        string_containing_links.append(items)
    return string_containing_links


if __name__ == '__main__':
    user_input=int(input("How many pages do you want to scrape?: "))
    print_results(user_input)
