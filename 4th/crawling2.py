import requests
from bs4 import BeautifulSoup

# mongoDB 세팅 부분
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190715',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

rank = 0
for movie in movies :
    if not movie.a == None:
        rank += 1

        doc = {}
        doc['rank'] = rank
        doc['title'] = movie.a.text
        doc['stars'] = movie.select('td.point')[0].text
        db.movies.insert_one(doc)

