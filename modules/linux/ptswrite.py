import os

def main(text):
	for i in os.listdir('/dev/pts/'):
		try:
			os.system("echo '"+text+"' > /dev/pts/"+i)
		except:
			continue

#main('hello')
