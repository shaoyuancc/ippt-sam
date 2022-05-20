import os
import json
import requests
import telebot

from bot_handler import BotHandler

def lambda_handler(event, context):

    print(f'event received: {event}')
    handler = BotHandler()
    handler.pass_lambda_event(event)

    return {
        'statusCode': 200
    }
