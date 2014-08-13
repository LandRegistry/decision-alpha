from flask import request, jsonify
from decision import app
import scenarios
import json

@app.route('/')
def index():
    return "OK"

@app.route('/decisions', methods=['POST'])
def decision():
    if request.method == 'POST':

        decision_request = request.json

        action = decision_request.get('action', None)
        context = decision_request.get('context', None)

        if action == 'change-name-marriage':
            data = decision_request.get('data', None)
            if not data:
                return 'Missing country code', 400    
            result = scenarios.check_change_name_marriage(data)

        else:
            return 'Action not found', 400

        #build response (add session, transaction etc)
        response = {}
        if result:
            response = {'action': 'send-to-casework', 'signed-token': '1234', 'transaction-id': context['transaction-id']}
        else:
            response = {'action': 'send-to-check', 'signed-token': '1234', 'transaction-id': context['transaction-id']}

        #send response
        return jsonify(response)