from flask import Flask

API_URL = "http://127.0.0.1:5000"
PRODUCTS_API_URL = API_URL + "/products"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Test api endpoint is running"

@app.route("/products")
def serve_json():
    return {
        "products": [
            {"name": "TST", "stock_quantity": 10}
        ]
    } #, 200, {'Content-Type': 'aplication/json; charset=utf-8'}
