from infraestructure.services.open_ai.service import OpenAiService
from infraestructure.services.kafka.service import KafkaService
from domain.character_events_preprompt import characterEventsPreprompt

class GetCaracterHistory:
    def call(characterName):
        characterIAData = OpenAiService.getChatGptChatCompletion(characterEventsPreprompt + characterName)
        KafkaService.sendMessage(characterIAData)
        return characterIAData

