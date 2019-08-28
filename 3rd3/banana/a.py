import requests
import smtplib
import schedule
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


def make_alarm(destination, from_date, to_date, passenger, target_price):
    url = "https://api.skypicker.com/flights?fly_from=SEL&fly_to=" + destination + "&date_from=" + from_date + "&date_to=" + from_date + "&return_from=" + to_date + "&return_to=" + to_date + "&adults=" + str(passenger) + "&curr=KRW&sort=price&partner=picky"
    result = requests.get(url)
    result_text = result.json()
    print (result_text)
    print (result_text['data'])
    price = result_text['data'][0]['price']

    if price <= int(target_price):
        return True
    else:
        return False

def sending_email(send_to_email):
    email = 'sending.scc.project@gmail.com'  # Your email
    password = 'scc123123!'  # Your email account password
    subject = '맞춤 가격의 비행기 티켓을 찾았습니다'
    messageHTML = '<p>여기 -> <a href="https://www.kiwi.com/ko/">링크<a> 를 눌러 원하는 가격의 티켓을 구매하세요! <span style="color: #588c7e">원하는 가격의 티켓과 함께 즐거운 여행을 계획하세요!</span><p>'

    msg = MIMEMultipart('alternative')
    msg['From'] = 'SPARTA TICKET FINDER'
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(messageHTML, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()


    db.tickets.update_one({'is_emailed':False,'email':send_to_email},{'$set':{'is_emailed': True}})

def get_db_data():
    tickets = db.tickets.find({'is_emailed':False},{'_id':0})
    for ticket in tickets:
        destination = ticket['destination']
        from_date = ticket['from']
        to_date = ticket['to']
        passenger = ticket['passenger']
        target_price = ticket['price']
        email = ticket['email']
        print('ticket info ----',destination,from_date,to_date,passenger,target_price)

        is_email = make_alarm(destination,from_date,to_date,passenger,target_price)
        if (is_email):
            print('sending..')
            sending_email(email)
        else:
            print('yet sending')

def job():
    print("정해진 시간이 됐으니 실행하자")
    get_db_data()

schedule.every(10).seconds.do(job)

def start():
    while True:
        print('돌아가고있니?')
        schedule.run_pending()
        time.sleep(1)