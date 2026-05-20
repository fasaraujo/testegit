from flask import Flask,jsonify,request

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

# ENDPOINTS

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

@app.route('/create_order', methods=['POST'])
def createPoOrder():
    arnaRequestData = request.get_json()
    arnaPurchaseOrder = {
        'id': arnaRequestData['id'],
        'description': arnaRequestData['description'],
        'items': []
    }

    po.append(arnaPurchaseOrder)
    return jsonify(arnaPurchaseOrder)

@app.route('/poitem/<int:id>/items')
def getPurchaseOrdersId(id):
    for i in po:
        if i['id'] == id:
            return jsonify(i['items']) 
    return jsonify({'message': f'pedido {id} nao encontrado'})

#
@app.route('/createpoiditems/<int:id>/items',methods=['POST'])
def createGetPoById(id):
    req_data = request.get_json()
    for i in po:
        if ( i['id'] == id ):
            i['items'].append({
                'id': req_data['id'],
                'description': req_data['description'],
                'price': req_data['price']
            })
            return jsonify(po)
    return jsonify({'message': f'pedido {id} nao encontrado'})

app.run(port=5000, debug=True)
