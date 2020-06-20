#######################################################################
#
#      PROJECT GEMINI 
#         AUTHOR : Ian Wright
#         github.com/ianwright27
#         thewian27@gmail.com 
#
#      "Stealing the source code doesn't make you the author"
#
#######################################################################
# MyBot
import sys
try:
	from chatterbot.trainers import ListTrainer # method to train
	from chatterbot import ChatBot # import the chatbot
	import os



	# ================  the bot ===============
	# 
	# 
	# 
	bot = ChatBot('bot',
			logic_adapters=[
		        'chatterbot.logic.MathematicalEvaluation',
		        'chatterbot.logic.SpecificResponseAdapter',
		        'chatterbot.logic.BestMatch'
		    ]
	    )

	# set trainer
	trainer = ListTrainer(bot)

	# select conversations and train the bot
	for file_ in os.listdir('convos'):
		conv = open('convos/'+file_, 'r').readlines()
		trainer.train(conv)


	# ================  additional libraries for real-app chatting ===============
	# 
	# 
	# 
	import json
	import requests
	import time
	from datetime import datetime
	import calendar

	instance_number= sys.argv[-3] #"88960"
	token = sys.argv[-2] #"nw1tu22ph3jx7kvd"
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
			if chat['self'] == 0:
				messages_to_reply_to.append(chat)

		return messages_to_reply_to


	# ================  MAIN LOOP (combines the chat bot and whatsapp api) ===============

	message = "hey, I am bot, hi" # bot's initial message

	while True:
		no_reply = True

		phone_numbers = literal_eval(sys.argv[-1]) # persons chatting with
		# phone_numbers = ["254779865684"] # persons chatting with

		for i in range(len(phone_numbers)):

			data = {"phone": phone_numbers[i],"body": message}
			
			# json_data = json.dumps(data)
			
			res = requests.post(url, data=data)

			# print (res.text, '\n Unix Timestamp:', spit_unixtime())
			print(f'bot: {message}') # output

			receiver = phone_numbers[0]+"@c.us"
			chatNumber = json.loads(res.text)['queueNumber']
			sent_time = spit_unixtime()
			
			# loop
			added_minute = 0
			while no_reply:
				time.sleep(10) # sleep 60 seconds / 1 minute
				added_minute += 1
				# max_delay = sent_time+(added_minute*60) # after one minute
				max_delay = spit_unixtime()

				PARAMS = {
				"token":token,"lastMessageNumber":chatNumber,
				"chatId":receiver,"limit":"20",
				"min_time":sent_time,"max_time":max_delay
				}

				_reply = fetch_reply(PARAMS, instance_number)
				if len(_reply) > 0:
					# drop all replies in last 20 seconds
					for text in _reply:
						name_of_receiver = text['chatName']
						message_ = text['body']

						print(f"{name_of_receiver} : {message_}") # output

					no_reply = False
					# chat here/modify message variable
					message = bot.get_response(message_) # bot response
			# end of loop 
except IndexError:
	print ("[+] Error!!! \nrun: \n\t\tmain.py INSTANCE_NUMBER TOKEN CONTACT_LIST")
	print("\n\n INSTANCE_NUMBER ->\t eg 88960\n")
	print("TOKEN ->\t eg nw1tu22ph3jx7kvd\n")
	print("CONTACT_LIST ->\t eg ['2547xxxxxx234', '234xxxxxx123']\n\t or if one just ['254xxxxx00']")
