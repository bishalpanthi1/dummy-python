import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    my_secret = os.environ.get('MY_SECRET', 'default-value')
    return f'Hello World! This is test Page'

if __name__ == '__main__':
    port_str = os.environ.get('PORT', '5000')
    port = int(port_str) if port_str.isdigit() else 5000
    app.run(host='0.0.0.0', port=port, debug=True)
