from flask import Flask, request
from infraestructure.services.open_ai.service import OpenAiService as aiService
from application.use_cases.get_character_history import GetCaracterHistory 

app = Flask(__name__)
@app.route('/', methods=['GET'])
def search():
    args = request.args
    if 'name' in args:
        return GetCaracterHistory.call(args['name'])
    return ('Name not found')

app.run(host='0.0.0.0', port=81)