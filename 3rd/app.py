from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

name = 'default'
age = 0
articles = []
articles_idx = 0




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
   return jsonify({'result':'success', 'msg': '이 요청은 POST!', name: name})

@app.route('/test', methods=['GET'])
def test_get():
   global name
   global age
   name = request.args.get('name')
   age = request.args.get('age')

   return jsonify({'result':'success', 'msg': '이 요청이ㅓㅏ니아ㅓㄹ니ㅏ얼은 GET!',name:name,age:age})

@app.route('/post', methods=['POST'])
def post_save():

    global articles
    global articles_idx

    link = request.form['link']
    comment = request.form['comment']
    articles_idx = articles_idx + 1
    article = {'articles_idx' : articles_idx, 'link':link, 'comment':comment}
    articles.append(article)

    return jsonify({'result':'success'})

@app.route('/view', methods=['GET'])
def get_view():
    return jsonify({'data' : articles, 'result' : 'success'})

@app.route('/delete', methods=['POST'])
def post_delete():
    global articles
    articles_idx = request.form['articles_idx']

    for testArticle in articles:
        if str(testArticle['articles_idx']) ==  articles_idx:
            articles.remove(testArticle)
            return jsonify({'result': 'success'})
    return jsonify({'result':'success','data':articles})
# testArticle['articles_idx'] 이건 dictionary형인가? // testArticle 이라는 변수에 전역변수로 선언 된 articles 의 값을 넣는다.
            # 왜 str을 써야하지? 오른쪽의 articles_idx가 문자열이라서?? 왼쪽은 그럼 숫자인가?
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
# def primenum(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print(i)
#             return  False
#         else:
#             return True
#
# print(primenum(11))
# print(primenum(17))


