import openai
from os import getenv


class Chatbot:
    def __init__(self):
        # Calls the api key and stores it
        openai.api_key = 'test'

    def get_response(self, user_input):
        # Set up for the chatbot
        response = openai.Completion.create(
            # Chatbot type
            engine="text-davinci-003",
            # User_input
            prompt=user_input,
            # Max amount of output given by bot
            max_tokens=4000,
            # Produce more accurate answer when the number is closer to zero but more diverse when closer to 1
            temperature=0.5
        ).choices[0].text

        return response


if __name__ == '__main__':
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
