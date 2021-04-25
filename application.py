from flask import Flask

print("name", __name__)

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/api/test')
def api_test():
    return {'results': ['great', 'fine', 'fanatastic']}