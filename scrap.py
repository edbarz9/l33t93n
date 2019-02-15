import os
from urllib.parse   import quote
from urllib.request import urlopen as uOpn
from urllib.request import urlretrieve as uRtv
from bs4 import BeautifulSoup as bsoup

base="https://rickandmorty.fandom.com/wiki/Category:Characters?from="

def soupMaker(url):
    uClient = uOpn(url)
    html_page = uClient.read()
    uClient.close()
    soup = bsoup(html_page,"html.parser")
    return soup

def letterScrap(letter, f):
    pagesoup = soupMaker(base + letter)
    nameUL = pagesoup.find('ul',{'class':'category-page__members-for-char'})
    nameLI = nameUL.find_all('a')
    for n in nameLI:
        n = n.get_text()
        if "Category:" not in n:
            print(n)
            f.write(n + "\n")

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

filename = "rick_and_morty"
f = open(filename,"w")

for letter in alphabet:
    letterScrap(letter,f)

f.close()
