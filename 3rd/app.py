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

# ## API 역할을 하는 부분
# @app.route('/test', methods=['POST'])
# def test_post():
#    name_receive = request.form['name_give']
#
#    # global 변수 name에 받은 것을 덮어쓰기
#    global name
#    name = name_receive
#    return jsonify({'result':'success', 'msg': '이 요청은 POST!', name : name })

@app.route('/test', methods=['GET'])
def test_get():

    global name
    global age
    name = request.args.get('name')
    age = request.args.get('age')
    return jsonify({'resulrt' : 'success', 'msg' : '이 요청은 GET!', name : name, age : age })

@app.route('/post', methods=['POST'])
def test_post():

    global articles
    global articles_idx
    link = request.form['link']
    comment = request.form['comment']
    category = request.form['category']
    articles_idx =  articles_idx + 1
    article = {'articles_idx' : articles_idx, 'link':link, 'comment' : comment}
    articles.append(article)

    article = {'link':link, 'comment':comment, 'category' : category}


    return jsonify({'result;':'success'})

@app.route('/view', methods=['GET'])
def get_view():
    return jsonify({'result': 'success','data':articles})

@app.route('/delete', methods=['POST'])
def pot_delete():
    global articles_idx
    articles_idx = request.form['articles_idx']
    for article in articles:
        if str(article['articles_idx']) == articles_idx:
            articles.remove(article)
        return jsonify({'result': 'success'})
        return jsonify({'result':'success','data':articles})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)





