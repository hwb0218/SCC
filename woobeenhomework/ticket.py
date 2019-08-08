from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017 )
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('ticket.html')


@app.route('/save', methods=['POST'])
def save():
    url_receive = 'http://www.onlinetour.co.kr/flight/international/booking/FareSearch?trip=RT&soto=N&startDt=20190816&endDt=20190830&startDtDesc=19%2F08%2F16&endDtDesc=19%2F08%2F30&sDate1=&sDate2=&sDate3=&sDate1Desc=&sDate2Desc=&sDate3Desc=&sCity1=SEL&eCity1=KIX&sCity2=KIX&eCity2=SEL&sCity3=&eCity3=&sCity1Desc=%EC%84%9C%EC%9A%B8%2F%EC%9D%B8%EC%B2%9C&eCity1Desc=%EC%98%A4%EC%82%AC%EC%B9%B4%28%EA%B0%84%EC%82%AC%EC%9D%B4%29&eCity2Desc=&sCity2Desc=%EC%98%A4%EC%82%AC%EC%B9%B4%28%EA%B0%84%EC%82%AC%EC%9D%B4%29&eCity3Desc=&sCity3Desc=&fareType=Y&adt=1&chd=0&inf=0&filterAirLine=&stayChk=&stayLength='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    tickets = soup.select('.gt_result_container')
    print(tickets)
    rank = 0
    for ticket in tickets:
        doc = {}
        # doc['rank'] = rank
        doc['title'] = ticket.select('.gt_trip_card_total_price > strong')[0].text.strip()
        # doc['singer'] = song.select('td.info > a')[1].text.strip()

        print(doc)
        db.gmarket.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/get', methods=['GET'])
def get():
    tickets = db.gmarket.find({}, {'_id': 0})
    return jsonify({'result': 'success', 'tickets': list(tickets)})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
