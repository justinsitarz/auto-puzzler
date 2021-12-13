from bs4 import BeautifulSoup
import requests
import re
import json
import os
from twilio.rest import Client
import random


def main():
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        file = "classic-puzzles.txt"
        puzzles = readPuzzles(file)
        ind = random.randrange(len(puzzles)
        nums = [""]
        sendSMS(nums, client, puzzles[ind])

def readPuzzles(filename):
    with open(filename) as f:
        puzzles = f.read().splitlines()
    return puzzles

def sendSMS(nums, client, puzzle):
        for num in nums:
            message = client.messages.create(body=puzzle, messaging_service_sid=os.environ['TWILIO_MS_SID'], to=num)

if __name__ == '__main__':
    main()
