import requests, os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from shutil import copyfile

quote_page = 'https://zh.wikipedia.org/wiki/2019%E5%B9%B4%E8%8F%AF%E8%AA%9E%E9%9B%BB%E5%BD%B1%E5%88%97%E8%A1%A8?fbclid=IwAR2oSwZrtKvDql51sQfd0cFkVNzhzIFV-Lq1g5Yg4mXAoRnANbD0ocGC2lQ'

r = requests.get(quote_page)
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

print('香港電影:')
sel = soup.select("#mw-content-text > div > table:nth-child(7) tr") #香港上映電影列表table
del(sel[0])

for s in sel:
    movieName = s.find_all('td')[1].text
    movieUrl = ''
    englishName = s.find_all('td')[2].text
    director = s.find_all('td')[3].text
    characters = s.find_all('td')[4].text

    # 下載圖片
    if s.find_all('td')[1].a:
        movieUrl = "https://zh.wikipedia.org/" + s.find_all('td')[1].a['href']
        r2 = requests.get(movieUrl)
        soup2 = BeautifulSoup(r2.text,"html.parser")
        pictureUrl = soup2.select("#mw-content-text > div > table.infobox.vevent > tbody > tr:nth-child(2) > td > a > img")
        if pictureUrl:
            downloadUrl = 'https:' + pictureUrl[0]['src']
            #print(pictureUrl[0]['src'])
            # headers = {'User-Agent': 'Mozilla/5.0'}
            # response = requests.get(url, headers=headers)  # 使用header避免訪問受到限制
            local = os.path.join('.\\HK_movies\\' + movieName + ".jpg")  #檔案儲存位置
            urlretrieve(downloadUrl,local)
            print(movieName + ' 下載完成!')
        else:
            copyfile("zhwiki.jpg", ".\\HK_movies\\" + movieName + ".jpg")
            print(movieName + ' 下載完成! (沒有圖片，用維基圖片替代)')


print('台灣電影:')
sel2 = soup.select("#mw-content-text > div > table:nth-child(9) tr") #台灣上映電影列表table
del(sel2[0])

for s in sel2:
    movieName = s.find_all('td')[1].text
    movieUrl = ''
    englishName = s.find_all('td')[2].text
    director = s.find_all('td')[3].text
    characters = s.find_all('td')[4].text

    # 下載圖片
    if s.find_all('td')[1].a:
        movieUrl = "https://zh.wikipedia.org/" + s.find_all('td')[1].a['href']
        r2 = requests.get(movieUrl)
        soup2 = BeautifulSoup(r2.text,"html.parser")
        pictureUrl = soup2.select("#mw-content-text > div > table.infobox.vevent > tbody > tr:nth-child(2) > td > a > img")
        if pictureUrl:
            downloadUrl = 'https:' + pictureUrl[0]['src']
            #print(pictureUrl[0]['src'])
            # headers = {'User-Agent': 'Mozilla/5.0'}
            # response = requests.get(url, headers=headers)  # 使用header避免訪問受到限制
            local = os.path.join('.\\TW_movies\\' + movieName + ".jpg")  #檔案儲存位置
            urlretrieve(downloadUrl,local)
            print(movieName + ' 下載完成!')
        else:
            copyfile("zhwiki.jpg", ".\\TW_movies\\" + movieName + ".jpg")
            print(movieName + ' 下載完成! (沒有圖片，用維基圖片替代)')