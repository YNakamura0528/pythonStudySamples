from bs4 import BeautifulSoup
import requests
import pandas as pd
# こちらで用意したHTML

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# BeautifulSoupの初期化

soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化

print("title")
print(soup.title.string)
print("--------")
links =soup.find_all("a")
for link in links:
    print(link.string)
    print(link)
    print(link.get("href"))

print("--------")

print("--------")
print("--------")

res = requests.get("https://www.galleon.blue/")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.find_all("a")
for link in links:
    print(link.get("href"))


print("--------")
print("--------")
print("--------")
df = pd.DataFrame([], columns = ["title", "url"])
entries = soup.find_all("h1", {"class": "entry-title"})
for entry in entries:
    sr = pd.Series([entry.a.string, entry.a.get("href")], index = ["title", "url"])
    df = df.append(sr, ignore_index = True)

print(df)
df.to_csv("test.csv")
