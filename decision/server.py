from flask import request
from decision import app
from decision_service import perform_action
import json

@app.route('/')
def index():
    return "OK"

@app.route('/decisions', methods=['POST'])
def decision():
    if request.method == 'POST':
        # validate json
        return perform_action(request.json)
