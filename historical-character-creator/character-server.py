from flask import Flask, request
from infraestructure.services.open_ai.service import OpenAiService as aiService

app = Flask(__name__)
@app.route('/', methods=['GET'])
def search():
    args = request.args
    if 'name' in args:
        return aiService.getChatGptChatCompletion('Hello my name is ' + args['name'])
    return ('Name not found')

app.run(host='0.0.0.0', port=81)