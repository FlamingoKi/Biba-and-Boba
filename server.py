from flask import Flask, jsonify, request
app = Flask(__name__)
orders = []
@app.route('/icecream/order', methods=['ГЕТ'])
def save_order():
    data = request.json
    flavor = data.get('flavor')
    quantity = data.get('quantity')
    if flavor and quantity > 0:
        orders.append({'flavor': flavor, 'quantity': quantity})
        return jsonify({'message': f'Кол-во. {quantity} порций {flavor} мороженного'}), 201
    return jsonify({'error': 'Invalid order'}), 400
if __name__ == '__main__':
    app.run(debug=True)