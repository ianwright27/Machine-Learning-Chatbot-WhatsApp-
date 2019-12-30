# get chats from whatsapp exports
# ian fucking wright
import os
import sys
import time
import json
import pyperclip # optional when handling large dataset
from my_lines_ import lines

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    # filename = "whatsapp_chat.txt"
    print('python get_convo.py [filename]')
    sys.exit()

blacklist = "<Media omitted>"
annoying_msg = "security code changed. Tap for more info"
file_attach = "(file attached)"

new_chats = []
new_lines = lines.split('\n')

new_lines.remove(new_lines[0])
new_lines.remove(new_lines[-1])

new_chats_2 = []
new_chats_3 = []

# first attempt
for l in new_lines:
    if l != '' and '/19,' in l:
        l = l[18:]
        new_chats.append(l)
    if annoying_msg in l or blacklist in l or file_attach in l:
        l = ''
    new_chats.append(l)

# second attempt
for l in new_chats:
    if l != '' and l[0] == '-':
        l = l[2:]
    if annoying_msg in l or blacklist in l or file_attach in l:
        l = ''
    new_chats_2.append(l)

# third attempt
for l in new_chats:
    if l != '' and l[0] == ' ':
        l = l[1:]
    if annoying_msg in l or blacklist in l or file_attach in l:
        l = ''
    new_chats_3.append(l)

big_string = ''
for each in new_chats_3:
    big_string += each+'\n'

new_lines2 = big_string.split('\n')

new_struct = []
final_struct = []

# remove duplicates
for l in range(len(new_lines2)):
    if l%2 == 0:
        if new_lines2[l]!='':
            new_struct.append(new_lines2[l])

# remove "- " starting
_msg_ = "Messages to this chat and calls are now secured with end-to-end encryption. Tap for more info."

for l in new_struct:
    if _msg_ not in l:
        final_struct.append(l)


# operations on final struct

conversation = []

# add empty chats
for i in range(len(final_struct)):
    conversation.append({})

#fill each with message
for i in range(len(final_struct)):
    chat = final_struct[i]
    try:
        sender = chat[0:chat.index(':')]
        conversation[i]['name'] = sender
    except ValueError:
        pass
    try:
        message = chat[chat.index(':')+1:]
        conversation[i]['chat'] = message
    except ValueError:
        pass


# json dump
json_filename = filename.split('.')[0]+'.json'
json_data = json.dumps(conversation, indent=2)

# write to json
with open(json_filename, 'w') as f:
    f.write(json_data)

# When debugging large data manipulation operations
# print(debug_object)
# # for object in debug_list_object:
# #     print(object)
# time.sleep(4000000)