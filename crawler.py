#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
import pdb
import datetime
import sys
from bs4 import BeautifulSoup

def googleNewsCrawler():
    filename = "google_news/{:%Y-%m-%d %H.%M.%S}.txt".format(datetime.datetime.now())

    res = requests.get("https://news.google.com")
    soup = BeautifulSoup(res.text, "html.parser")
    #print soup.select(".esc-body")

    count = 1

    f = open(filename, 'w+')

    for item in soup.select(".esc-body"):
        print '========[',count,']========='
        news_title = item.select(".esc-lead-article-title")[0].text
        news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
        print news_title
        print news_url
        try:
            news_res = requests.get(news_url)
            text_split = re.compile('<p class=\"first\">.*</p>|<p>.*</p>')
            #text = str(text_split.findall(news_res.text)).replace('<p class=\"first\">', '').replace('</p>', '').replace(' ', '').replace('<p>', '').replace('[', '').replace(']', '').replace('\',\'', '')
            text_list = text_split.findall(news_res.text)
            try:
                text = text_list[0].replace('<p class=\"first\">', '').replace('</p>', '').replace(' ', '').replace('<p>','').replace('[', '').replace(']', '').replace('\',\'', '')
                for item in text_list[1:]:
                    text += item.replace('<p class=\"first\">', '').replace('</p>', '').replace(' ', '').replace('<p>','').replace('[', '').replace(']', '').replace('\',\'', '')
                f.write(news_title.encode('utf-8')+" "+text.replace(',',' ').encode('utf-8')+"\n")
            except:
                f.write(news_title.encode('utf-8')+"\n")
            #for passage in soup.select("<p>"):
            #    print passage
        except:
            print "Error connection to:",news_url
        count += 1
    f.close()
    return filename

def crawler_main():
    filename = googleNewsCrawler()
    print "File saved to: ",filename
    return filename

if __name__ == "__main__":
    filename = crawler_main()
