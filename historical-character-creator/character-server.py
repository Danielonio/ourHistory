from flask import Flask, request
from infraestructure.services.open_ai.client import OpenAiCLient as aiClient

app = Flask(__name__)
@app.route('/', methods=['GET'])
def search():
    args = request.args
    if 'name' in args:
        url = "https://api.openai.com/v1/chat/completions"
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello!"}]
        }
        response = aiClient.post(url, data)
        return response['choices'][0]['message']['content']
    return ('Name not found')

app.run(host='0.0.0.0', port=81)