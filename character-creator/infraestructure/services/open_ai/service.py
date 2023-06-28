from .client import OpenAiClient as client

class OpenAiService:
    def getChatGptChatCompletion(prompt: str):
        completionUrl = 'https://api.openai.com/v1/chat/completions'
        body = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': prompt}]
        }
        response = client.post(completionUrl, body)
        return response['choices'][0]['message']['content']
         


    

