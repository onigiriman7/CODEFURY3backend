from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#Create a chatbot
chatbot=ChatBot('Helper')
trainer = ListTrainer(chatbot)


for _file in os.listdir('../chat_train'):
    chats = open('../chat_train/'+_file, 'r').readlines()
    trainer.train(chats)
