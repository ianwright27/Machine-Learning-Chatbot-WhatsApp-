import os
import sys


def main(PATH):
	for file_ in os.listdir(PATH):
		os.system("echo lines=''' > my_lines_.py")
		os.system(f'type {file_} >> my_lines_.py')
		os.system("echo ''' >> my_lines.py")

		# run get_convo.py
		os.system(f"python get_convo.py {file_}")

if len(sys.argv) < 2:
	print('\npython what2json.py [PATH]')
else:
	PATH = sys.argv[1]
	main(PATH)
