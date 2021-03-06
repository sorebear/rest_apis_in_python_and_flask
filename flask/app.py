from flask import Flask, jsonify

app = Flask(__name__)
# JSON is basically a Dictionary - See Below
stores = [
    {
        'name': 'Wally\'s Store',
        'items': [
            {
                'name': 'Brocolli',
                'price': .99
            },
            {
                'name': 'Spinach',
                'price': .49
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>') 
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass

app.run(port=4000)
