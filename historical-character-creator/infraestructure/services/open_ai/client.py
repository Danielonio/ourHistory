import os
import requests
from dotenv import load_dotenv

class OpenAiCLient:
  load_dotenv() 
  api_key = os.environ.get('OPENAI_API_KEY')
  headers = {
      'Authorization': 'Bearer %s' % (api_key)
  }

  def post(url:str, body:object):
    postResponse = requests.post(url, json=body, headers=OpenAiCLient.headers)
    postResponseJson = postResponse.json()
    return postResponseJson