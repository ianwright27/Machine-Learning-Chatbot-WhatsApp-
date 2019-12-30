import os, sys, subprocess, time

def main(PATH):
	
	for file_ in os.listdir('.'):

		ext = file_.split('.')[-1]
		
		if 'txt' in ext and file_[0] == 'W':
			
			print('file: ',file_)

			subprocess.run("echo lines=''' > my_lines_.py", shell=True)

			subprocess.run(f"type {file_} >> my_lines_.py", shell=True)

			subprocess.run("echo ''' >> my_lines_.py", shell=True)

			# run get_convo.py
			subprocess.run(f"python get_convo.py {file_}", shell=True)

if len(sys.argv) < 2:
	
	print('\npython what2json.py [PATH]')

else:

	PATH = sys.argv[1]

	main(PATH)
