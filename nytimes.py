from urllib.request import urlopen
import pandas as pd
import xml.etree.ElementTree as et
import requests
from bs4 import BeautifulSoup

URL = "https://www.nytimes.com/sitemaps/new/news.xml.gz"
response = requests.get(URL)
with open('news.xml', 'wb') as f:
    f.write(response.content)

tree = et.parse("news.xml")
root = tree.getroot()
checked_list = ["virus","corona","disease","cold","cough"]

article_list = []
for child in root:
    url = child[0].text
    get_url = requests.get(url)
    get_text = get_url.text
    soup = BeautifulSoup(get_text, "html.parser")

    header = soup.find('h1')
    if any([True if word in header.text.lower() else False for word in checked_list]):
        print("Found Article -->  ",url)
article_list.append(url)

def parse_website(url):
    content = {}
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    #this is specific to new york times headlines as far as I can see
    title_box = soup.find('div', attrs={'class': 'css-1vkm6nb ehdk2mb0'}).h1
    title = title_box.text.strip()
    body_companion = soup.find_all('h2',attrs={'class':'css-3ez4hu eoo0vm40'})
    subtitles = [body.text.strip() for body in body_companion]
    body = soup.find_all('p',attrs={'class':'css-exrw3m evys1bk0'})
    body_list = [item.text.strip() for item in body]
    content['title'] = title
    content['subtitles'] = subtitles
    content['body']=body_list
    return content

