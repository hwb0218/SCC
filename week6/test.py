print ('Hello World')
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

name = 'empty'

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   # name_give를 받는 부분
   name_receive = request.form['name_give']

   # global 변수 name에 받은 것을 덮어쓰기
   global name
   name = name_receive

   return jsonify({'result':'success'})

@app.route('/test', methods=['GET'])
def test_get():
   # global 변수 name을 보여주기
   return jsonify({'result':'success', 'name': name})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)