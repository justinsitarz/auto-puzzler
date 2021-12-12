from bs4 import BeautifulSoup
import requests
import re
import json
import os
from twilio.rest import Client
import logger

logging.basicConfig(level=logging.DEBUG, filename='app.log')

def main()
	account_sid = os.environ['TWILIO_ACCOUNT_SID']
	auth_token = os.environ['TWILIO_AUTH_TOKEN']
	client = Client(account_sid, auth_token)
	source_url = "https://www.npr.org/series/4473090/sunday-puzzle"
	soup = str(BeautifulSoup(requests.get(source_url).text, 'html.parser'))
	m = re.search("\"Click Featured Story Image 1-1\",\"category\":\"Aggregation\"}\' href=\"(.*)\"", soup)
	puzzle_soup = str(BeautifulSoup(requests.get(m.group(1)).text, 'html.parser'))
	puzzle = re.search("This week's challenge: <\/strong>([\w\-\s',.\"]*)<\/p>", puzzle_soup).group(1)
	body = "NPR Sunday Puzzler: {}".format(puzzle)
	nums = []
	sendSMS(nums, client)
	logging.info('Puzzle text: {}'.format(body))


def sendSMS(nums, client)
	for num in nums: 
		message = client.messages.create(body=puzzle, messaging_service_sid=os.environ['TWILIO_MS_SID'], to=num)
		logging.info("Message SID: {}".format(message.sid))


if __name__ == '__main__':
    main()
