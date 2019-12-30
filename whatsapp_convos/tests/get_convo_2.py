import json
from my_lines_ import lines

new_lines = lines.split('\n')

new_lines.remove(new_lines[0])
new_lines.remove(new_lines[-1])

new_struct = []
final_struct = []

# remove duplicates
for l in range(len(new_lines)):
	if l%2 == 0:
		new_struct.append(new_lines[l])

# remove "- " starting
for l in new_struct:
	if l!='' and l[0]=='-' and l[1]==' ':
		l = l[2:]
		final_struct.append(l)

# get total number of messages
# count = 0
# for i in final_struct:
# 	count+=1
# 	print(count,i)

# operations on final struct
conversation = []
# add empty chats
for i in range(len(final_struct)):
	conversation.append({})

#fill each with message
for i in range(len(final_struct)):
	chat = final_struct[i]
	sender = chat[0:chat.index(':')]
	message = chat[chat.index(':')+1:]
	conversation[i]['name'] = sender
	conversation[i]['chat'] = message

# json dump
json_data = json.dumps(conversation, indent=2)
with open('whatsapp_chat.json', 'w') as f:
	f.write(json_data)