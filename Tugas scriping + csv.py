#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://proxyway.com/reviews'
reviews_list = []

# Melakukan permintaan HTTP GET ke URL
response = requests.get(URL)
soup = bs(response.content, 'html.parser')

# Mengambil data ulasan
reviews = soup.find_all('div', class_='review-item')

for review in reviews:
    d = {}
    d['Reviewer'] = review.find('span', class_='reviewer-name').text.strip()
    d['Rating'] = review.find('span', class_='reviewer-rating').text.strip()
    d['Comment'] = review.find('div', class_='review-text').text.strip()
    reviews_list.append(d)

# Menyimpan data ke dalam file CSV
filename = 'reviews.csv'
fieldnames = ['Reviewer', 'Rating', 'Comment']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reviews_list)

print("Scraping selesai. Data telah disimpan ke dalam file CSV.")


# In[2]:


import requests
from bs4 import BeautifulSoup

start_url = "https://proxyway.com/news"

def scrape_page(url):
    print("URL : " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print("DONE")
        
def get_data(content):
    pass

def main():
    scrape_page(start_url)
    
if __name__ == "__main__":
    main()


# In[3]:


import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://proxyway.com/news"
news_list = []

def scrape_page(url):
    print("URL : " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print("DONE")
        
def get_data(content):
    articles = content.find_all("article", class_="post-card")
    for article in articles:
        d = {}
        d['Title'] = article.find("h2", class_="post-card_title").text.strip()
        d['Date'] = article.find("span", class_="post-card_date").text.strip()
        d['Author'] = article.find("span", class_="post-card_author").text.strip()
        news_list.append(d)

def main():
    scrape_page(start_url)
    
    # Menyimpan data ke dalam file CSV
    filename = 'news.csv'
    fieldnames = ['Title', 'Date', 'Author']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(news_list)
    
    print("Scraping selesai. Data telah disimpan ke dalam file CSV.")

if __name__ == "__main__":
    main()


# In[ ]:


import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://proxyway.com/news"
news_list = []

def scrape_page(url):
    print("URL : " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print("DONE")
        
def get_data(content):
    articles = content.find_all("article", class_="post-card")
    for article in articles:
        d = {}
        title_element = article.find("h2", class_="post-card_title")
        if title_element:
            d['Title'] = title_element.text.strip()
        else:
            d['Title'] = ''
            
        date_element = article.find("span", class_="post-card_date")
        if date_element:
            d['Date'] = date_element.text.strip()
        else:
            d['Date'] = ''
            
        author_element = article.find("span", class_="post-card_author")
        if author_element:
            d['Author'] = author_element.text.strip()
        else:
            d['Author'] = ''
        
        news_list.append(d)

def main():
    scrape_page(start_url)
    
    # Menyimpan data ke dalam file CSV
    filename = 'newss.csv'
    fieldnames = ['Title', 'Date', 'Author']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(news_list)
    
    print("Scraping selesai. Data telah disimpan ke dalam file CSV.")

if __name__ == "__main__":
    main()


# In[ ]:


import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://proxyway.com/news"
news_list = []

def scrape_page(url):
    print("URL : " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print("DONE")
        
def get_data(content):
    articles = content.find_all("article", class_="post-card")
    for article in articles:
        d = {}
        title_element = article.find("h2", class_="post-card_title")
        if title_element:
            d['Title'] = title_element.text.strip()
        else:
            d['Title'] = ''
            
        date_element = article.find("span", class_="post-card_date")
        if date_element:
            d['Date'] = date_element.text.strip()
        else:
            d['Date'] = ''
            
        author_element = article.find("span", class_="post-card_author")
        if author_element:
            d['Author'] = author_element.text.strip()
        else:
            d['Author'] = ''
        
        news_list.append(d)

def main():
    scrape_page(start_url)
    
    # Menyimpan data ke dalam file CSV
    filename = 'newssss.csv'
    fieldnames = ['Title', 'Date', 'Author']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(news_list)
    
    print("Scraping selesai. Data telah disimpan ke dalam file CSV.")

if __name__ == "__main__":
    main()


# In[ ]:


import csv

# Data hasil scraping
scraped_data = [
    {'URL': 'https://proxyway.com/news'},
    {'URL': 'https://proxyway.com/news/page/2'},
    {'URL': 'https://proxyway.com/news/page/3'},
    {'URL': 'https://proxyway.com/news/page/4'},
    {'URL': 'https://proxyway.com/news/page/5'},
    {'URL': 'https://proxyway.com/news/page/6'}
]

# Menentukan nama file CSV
filename = 'scraped_data.csv'

# Menentukan header kolom
fieldnames = ['URL']

# Menulis data ke dalam file CSV
with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Menulis header kolom
    writer.writeheader()

    # Menulis baris data
    writer.writerows(scraped_data)

print("File CSV berhasil dibuat dengan nama:", filename)


# In[ ]:




