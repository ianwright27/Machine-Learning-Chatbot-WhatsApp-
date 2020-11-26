

### No releases yet

# Machine Learning Chatbot (WhatsApp)
1) "convos/" directory -> load all your conversational data set here 
                       in the format as the sample datasets already saved there.

2) Get an account from https://api.chat-api.com to get TOKEN and INSTANCE_NUMBER
#### Requires WhatsApp API ofcourse
3) open a command line window in main directory and run this
	python main.py INSTANCE_NUMBER TOKEN CONTACT_LIST


the arguments:

	INSTANCE_NUMBER ->	 eg 88960

	TOKEN ->	 		 eg nw1tu22ph3jx7kvd

	CONTACT_LIST ->	     eg ['2547xxxxxx234', '234xxxxxx123']
					     or if just one phone number to chat with -> ['254xxxxx00']


EXAMPLE:

	python main.py 88960 nw1tu22ph3jx7kvd ['254xxxxx00']
	python main.py 88960 nw1tu22ph3jx7kvd ['254xxxxx00', '254xxxxx00', '254xxxxx00']"# AI-Whatsapp-chat" 
