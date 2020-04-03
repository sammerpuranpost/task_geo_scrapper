from urllib.request import urlopen
import pandas as pd
import xml.etree.ElementTree as et
import requests
from bs4 import BeautifulSoup


class NyScraper:

    def __init__(self,url):
        self.url = url

    def get_parse_articles(self):
        response = requests.get(self.url)
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


            article_list.append(url)
        print(article_list[0])
        return self.parse_website(article_list[2])

    def parse_website(self,url):
        content = {}
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup)
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




