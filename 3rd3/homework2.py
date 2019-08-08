from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

order_sheets = []

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order_list')
def order_list():
   return render_template('order_list.html')

@app.route('/order_index')
def order():
   return render_template('order.html')
#
# @app.route('/order_data')
# def order_data():
#    return jsonify({'orders': order_sheets, 'result' : 'success'})

@app.route('/order' , methods=['POST'])
def post_order():

   global order_sheets

   name_receive = request.form['name_give']
   count_receive = request.form['count_give']
   address_receive = request.form['address_give']
   phone_reecive = request.form['phone_give']

   order_sheet = {'name' : name_receive , 'count' : count_receive , 'address' : address_receive , 'phone' : phone_reecive}
   order_sheets.append(order_sheet)

   return jsonify({'result': 'success'})


@app.route('/order' , methods=['GET'])
def get_order_view():

    return jsonify({'data' : order_sheets , 'result' : 'success'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)