from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

order_sheets = []

@app.route('/order' , methods=['POST'])
def post_order():

   global order_sheets

   name_receive = request.form['name_give']
   quantity_receive = request.form['quantity_give']
   address_receive = request.form['address_give']
   phonenum_reecive = request.form['phonenum_give']

   order_sheet = {'name_give' : name_receive , 'quantity_give ' : quantity_receive , 'address_give' : address_receive , 'phonenum_give' : phonenum_reecive}
   order_sheets.append(order_sheet)

   return jsonify({'result': 'success'})


@app.route('/view' , methods=['GET'])
def get_order_view():

    return jsonify({'data' : order_sheets , 'result' : 'success'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)