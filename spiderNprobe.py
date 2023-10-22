# https://en.wikipedia.org/wiki/Computer_programming

from mechanize import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

def spider_urls(url, keywords):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")    
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all("a")
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)




    for urls2 in urls:
        if urls2 not in visited_urls:
            visited_urls.add(urls2)
            url_join = urljoin(url, urls2)
            if keyword in url_join:
                print(url_join)
                spider_urls(url_join, keywords)
        else:
            pass






# http://yahoo.com


urls = input("Enter the URL you want ti scrap. ")
keyword = input("Enter the keyword to search for in the URL privided. ")

spider_urls(urls, keyword)