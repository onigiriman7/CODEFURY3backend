#import libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


#Create a chatbot
chatbot=ChatBot('Helper')
trainer = ListTrainer(chatbot)


request = input('You: ')
response = chatbot.get_response(request)
print('Helper: ', response)
request2 = input('You: ')
response2 = chatbot.get_response(request2)
print('Helper: ', response2)


#training on english dataset
