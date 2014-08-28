from flask import request
from decision import app
from decision_service import perform_action

@app.route('/')
def index():
    return "OK"


@app.route('/decisions', methods=['POST'])
def decision():
   return perform_action(request.json, app.config['CASEWORK_URL'], app.config['CHECK_URL'])
