from flask import request
from decision import app

@app.route('/')
def index():
    return "OK"

@app.route('/decisions', methods=['POST'])
def decision():
    if request.method == 'POST':
    	return '', 200
