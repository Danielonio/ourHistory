import os
from flask import Flask, request
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
@app.route('/', methods=['GET'])
def search():
    args = request.args
    if 'name' in args:
        load_dotenv() 
        api_key = os.environ.get('OPENAI_API_KEY')
        url_post = "https://api.openai.com/v1/chat/completions"
        new_data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello!"}]
        }
        headers = {
            'Authorization': 'Bearer %s' % (api_key)
        }
        post_response = requests.post(url_post, json=new_data, headers=headers)
        post_response_json = post_response.json()
        print(post_response_json)
        return post_response_json['choices'][0]['message']['content']
    return ('Name not found')

app.run(host='0.0.0.0', port=81)