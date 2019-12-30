import json
import requests
import time
from datetime import datetime
import calendar


# configs
instance_number= "88960"
token = "nw1tu22ph3jx7kvd"
url = f'https://eu92.chat-api.com/instance{instance_number}/message?token={token}'
no_reply = True

# Get unix time stamp of now
def spit_unixtime():
	d = datetime.utcnow()
	unixtime = calendar.timegm(d.utctimetuple())
	return unixtime

def fetch_reply(parameters_, instance_number):
	url2 = f"https://api.chat-api.com/instance{instance_number}/messages"
	PARAMS = parameters_
	r = requests.get(url2, params = PARAMS)
	json_data = json.loads(r.text)

	messages_to_reply_to = []
	for chat in json_data['messages']:
		# phone_ = chat['id'][5:17]
		# msg_ = chat['body']
		# print(f"{phone_}: {msg_}")
		if chat['self'] == 0:
			messages_to_reply_to.append(chat)

	# print(messages_to_reply_to)
	# for chat_object in messages_to_reply_to:
	# 	print(chat_object['body'])
	return messages_to_reply_to



message = input('You: ')
while True:
	no_reply = True

	phone_numbers = ["254779865684"] # persons chatting with

	for i in range(len(phone_numbers)):

		data = {"phone": phone_numbers[i],"body": message}
		
		json_data = json.dumps(data)
		
		res = requests.post(url, data=data)

		# print (res.text, '\n Unix Timestamp:', spit_unixtime())

		receiver = phone_numbers[0]+"@c.us"
		chatNumber = json.loads(res.text)['queueNumber']
		sent_time = spit_unixtime()
		
		# loop
		added_minute = 0
		while no_reply:
			time.sleep(20) # sleep 60 seconds / 1 minute
			added_minute += 1
			# max_delay = sent_time+(added_minute*60) # after one minute
			max_delay = spit_unixtime()

			PARAMS = {
			"token":"nw1tu22ph3jx7kvd","lastMessageNumber":chatNumber,
			"chatId":receiver,"limit":"20",
			"min_time":sent_time,"max_time":max_delay
			}

			_reply = fetch_reply(PARAMS, instance_number)
			if len(_reply) > 0:
				# drop all replies in last 20 seconds
				for text in _reply:
					name_of_receiver = text['chatName']
					message = text['body']
					print(f"{name_of_receiver} : {message}")

				no_reply = False
				# chat here/modify message variable
				message = input('You: ')
		# end of loop 
