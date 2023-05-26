from infraestructure.services.open_ai.service import OpenAiService as aiService
from domain.character_events_preprompt import characterEventsPreprompt

class GetCaracterHistory:
    def call(characterName):
        return aiService.getChatGptChatCompletion(characterEventsPreprompt + characterName)

