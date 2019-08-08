from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
    url_receive = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190715'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    rank = 0
    for song in songs:
        doc = {}
        # doc['rank'] = rank
        doc['title'] = song.select('td.info > a')[0].text.strip()
        # doc['singer'] = song.select('td.info > a')[1].text.strip()

        print(doc)
        db.genie.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/get', methods=['GET'])
def get():
    songs = db.genie.find({}, {'_id': 0})
    return jsonify({'result': 'success', 'songs': list(songs)})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
