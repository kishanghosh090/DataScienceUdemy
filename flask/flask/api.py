from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def api_data():
    query = request.args.get('query')
    data = {'results': [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Steve'},
        {'id': 3, 'name': 'Bill'},
    ]}
    if query:
        data['results'] = [item for item in data['results'] if query in item['name']]
    return jsonify(data)

@app.route('/')
def home():
    return "Welcome to The API"


if __name__ == "__main__":
    app.run(debug=True)