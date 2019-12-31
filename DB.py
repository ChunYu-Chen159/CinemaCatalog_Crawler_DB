import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient(host='140.121.196.23', port=4118)
# client = MongoClient('mongodb://localhost:4118/')
db = client.Movies
collection = db.Movie


quote_page = 'https://zh.wikipedia.org/wiki/2019%E5%B9%B4%E8%8F%AF%E8%AA%9E%E9%9B%BB%E5%BD%B1%E5%88%97%E8%A1%A8?fbclid=IwAR2oSwZrtKvDql51sQfd0cFkVNzhzIFV-Lq1g5Yg4mXAoRnANbD0ocGC2lQ'

r = requests.get(quote_page)
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

print('香港電影:')
sel = soup.select("#mw-content-text > div > table:nth-child(7) tr") #香港上映電影列表table
del(sel[0])
for s in sel:
    movieName = s.find_all('td')[1].text
    englishName = s.find_all('td')[2].text
    director = s.find_all('td')[3].text
    characters = s.find_all('td')[4].text
    img_url = 'http://140.121.196.23:4107/HK_movies/' + movieName + '.jpg'

    movie = {
        'movie_name': movieName,
        'english_name': englishName,
        'director': director,
        'characters': characters,
        'price': '250',
        'category': 'HK',
        'img_url': img_url
    }

    result = collection.insert_one(movie)
    print(result)



print('台灣電影:')
sel2 = soup.select("#mw-content-text > div > table:nth-child(9) tr") #台灣上映電影列表table
del(sel2[0])
for s in sel2:
    movieName = s.find_all('td')[1].text
    englishName = s.find_all('td')[2].text
    director = s.find_all('td')[3].text
    characters = s.find_all('td')[4].text
    img_url = 'http://140.121.196.23:4107/TW_movies/' + movieName + '.jpg'

    movie = {
        'movie_name': movieName,
        'english_name': englishName,
        'director': director,
        'characters': characters,
        'price': '250',
        'category': 'TW',
        'img_url': img_url
    }

    result = collection.insert_one(movie)
    print(result)
