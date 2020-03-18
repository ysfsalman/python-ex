import time
import threading

def run():
	x = 0
	while True:
		x +=1
		print(x)
		time.sleep(0.5)
		break 

if __name__ == "__main__":
	thread = threading.Thread(target=run, args=())
	thread.start()


	for i in range(500):
		print('a')
		time.sleep(0.25)
	
