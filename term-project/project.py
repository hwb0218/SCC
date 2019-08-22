from flask import Flask, render_template, jsonify, request
import requests
import schedule
import time
import smtplib

from email.mime.text import MIMEText
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)

s = smtplib.SMTP('smtp.gmail.com', 587)

def job():
    #     1.db디비에 있는걸 꺼내오고
    #     2.조건에 맞는걸 찾고
    #     3.맞으면 이메일을 보내주고
    data = db.tickets.find({}, {'_id': 0})
    data_list = list(data)
    for A in data_list:
        to = A['to']
        destination = A['destination']
        from_data = A['from']
        passenger = A['passenger']
        target_price = A['price']

    link = "https://api.skypicker.com/flights?fly_from=SEL&fly_to=" + destination + "&date_from=" +from_data+ "&date_to=" +from_data+ "&return_from=" + to + "&return_to=" + to + "&adults=" + passenger + "&curr=KRW&sort=price&partner=picky"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    ticket_data = requests.get(link, headers=headers)
    target = ticket_data['data'][0]['price']
    if  target >= target_price:
        msg = MIMEText('내용 : 메일 보내기 테스트 ')

        msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'

        s.sendmail("hwb0218@gmail.com", "hwb0218@naver.com", msg.as_string())

        s.quit()

        print("I'm working...")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/list')
def home_list():
    return render_template('order_list.html')


@app.route('/save', methods=['POST'])
def saving():
    firstName_receive = request.form['firstName_give']
    lastName_receive = request.form['lastName_give']
    to_receive = request.form['to_give']
    from_receive = request.form['from_give']
    email_receive = request.form['email_give']
    departure_receive = request.form['departure_give']
    destination_receive = request.form['destination_give']
    passenger_receive = request.form['passenger_give']
    price_receive = request.form['price_give']
    ticket = {

        'firstName': firstName_receive,
        'lastName': lastName_receive,
        'to': to_receive,
        'from': from_receive,
        'email': email_receive,
        'departure': departure_receive,
        'destination': destination_receive,
        'passenger': passenger_receive,
        'price' : price_receive
    }
    db.tickets.insert_one(ticket)
    return jsonify({'result': 'success'})


@app.route('/save', methods=['GET'])
def get_view():
    save = db.tickets.find({}, {'id': 0})
    return jsonify({'result': 'success', 'tickets': list(save)})


if __name__ == '__main__':

    s.starttls()

    s.login('hwb0218@gmail.com', 'vfmbbnnkrxdfcgwc')

    #
    # schedule.every(1).second.do(job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    app.run('0.0.0.0', port=5002, debug=True)