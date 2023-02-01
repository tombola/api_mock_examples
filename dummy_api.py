from bottle import route, run, template, get

@route('/')
def index(name):
    return "Test api endpoint is running"

@get('/products')
def serve_json():
    return {
        "products": [
            {"name": "TST", "stock_quantity": 10}
        ]
    }

run(host='localhost', port=8080)