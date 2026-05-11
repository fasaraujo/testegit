from flask import Flask,jsonify

app = Flask(__name__)

po = [
{
    'id':1,
    'descricao': 'pedido de compra 1',
    'items': [
        {
            'id':1,
            'description':'item do pedido 1',
            'price':10.55
        }
    ]
}

]

# criacao dos endpoins 

@app.route('/')
def home():
    return 'Hello Guys!! This is my first flask run..'

@app.route('/po')
def getpo():
    return jsonify(po)

@app.route('/po/<int:id>')
def getPoById(id):
    for i in po:
        if ( i['id'] == id ):
            return jsonify(i)
    return jsonify({'message': f'pedido {id} nao encontrado'})


app.run(port=5000, debug=True)
