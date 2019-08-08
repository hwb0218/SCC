from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)

articles = []
article_no = 1

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

# ## API 역할을 하는 부분
# @app.route('/post', methods=['POST'])
# def post():
#
#    url_receive = request.form['url_give']          # 클라이언트로부터 url을 받는 부분
#    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
#
#    article = {'url':url_receive,'comment':comment_receive} # 받은 걸 딕셔너리로 만들고,
#
#    db.articles.insert_one(article)
#
#    return jsonify({'result':'success'})

## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():
   url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
   comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get(url_receive, headers=headers)

   soup = BeautifulSoup(data.text, 'html.parser')

   og_image = soup.select_one('meta[property="og:image"]')
   og_title = soup.select_one('meta[property="og:title"]')
   og_description = soup.select_one('meta[property="og:description"]')
   og_locale = soup.select_one('meta[property="og:locale"]')


   url_image = og_image['content']
   url_title = og_title['content']
   url_description = og_description['content']
   url_locale = og_locale['content']

   article = {
      'url': url_receive,
      'comment': comment_receive,
      'image': url_image,
      'title': url_title,
      'desc': url_description,
      'locale' : url_locale
   }

   db.articles.insert_one(article)

   return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def view():
   posts = db.articles.find({}, {'_id': 0})
   return jsonify({'result':'success', 'articles':list(posts)})


@app.route('/delete', methods=['post'])
def delete():
   global articles                               # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.
   no_receive = request.form['no_give']          # 클라이언트로부터 no를 받는 부분

   for article in articles:                      # 반복문: articles를 돌면서,
       if str(article['no']) == no_receive:      # 조건문: 받은 no와 같은 번호의 아티클을 찾아서 (단, 문자열 == 문자열로!)
           articles.remove(article)              # 해당 article을 지우고,
           return jsonify({'result':'success'})  # 결과를 주고 함수를 끝낸다.

   return jsonify({'result':'fail', 'msg':'아티클이 없습니다'}) # 만약 반복문을 다 돌아도 결과를 주지 않았으면, 아티클이 없다고 한다.

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)