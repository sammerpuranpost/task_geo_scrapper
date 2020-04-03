from nytimes import NyScraper
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation as LDA
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_topics_from_body(article_dict):
    list_of_paragraphs = article_dict['body']
    list_of_paragraphs1 = ','.join(list_of_paragraphs)
    print(list_of_paragraphs1)
    wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    # Generate a word cloud
    wcloud = wordcloud.generate(list_of_paragraphs1)
    # Visualize the word cloud
    plt.figure()
    # plot words
    plt.imshow(wcloud, interpolation="bilinear")
    # remove axes
    plt.axis("off")
    # show the result
    plt.show()


nyscraper = NyScraper("https://www.nytimes.com/sitemaps/new/news.xml.gz")
article_dict = nyscraper.get_parse_articles()
get_topics_from_body(article_dict=article_dict)


