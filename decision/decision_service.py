from flask import request, jsonify, Response
import json
import scenarios

def decision_response_builder(result, context):
    #build response (add session, transaction etc)
    if result:
        return {'action': 'send-to-casework', 'signed-token': '1234', 'transaction-id': context['transaction-id']}
    else:
        return {'action': 'send-to-check', 'signed-token': '1234', 'transaction-id': context['transaction-id']}

def make_error_response(msg):
    js = {'error_message': msg }
    return Response(json.dumps(js), status = 400, mimetype='application/json')

def perform_action(decision_request):
    action = decision_request.get('action', None)
    context = decision_request.get('context', None)
    
    if action == 'change-name-marriage':
        data = decision_request.get('data', None)
        if not data:
            return make_error_response('Missing country code')
        result = scenarios.check_change_name_marriage(data)
        return jsonify(decision_response_builder(result, context))
    else:
        return make_error_response('Action not found')