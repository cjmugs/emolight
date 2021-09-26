import unicornhat as uh
import time

uh.set_layout(uh.PHAT)
uh.brightness(.7)


def happy():
    uh.set_all(0, 255, 0)
    uh.show()
    time.sleep(5)
    uh.clear()

def unhappy():
    uh.set_all(255, 165, 0)
    uh.show()
    time.sleep(5)
    uh.clear()

def angry():
    uh.set_all(255, 0, 0)
    uh.show()
    time.sleep(5)
    uh.clear()

def unknown():
    uh.set_all(0, 0, 255)
    uh.show()
    time.sleep(5)
    uh.clear()

def qnada():
    print("How are you feeling today?")
    good = 'good'
    mad = 'mad'
    sad = 'sad'
    unknown =  '?'
    response = input(' ')
    while True:
    	if response == good:
    		happy()
    		
    	elif response == sad:
    		unhappy()
    	
    	elif response == mad:
    		angry()

        elif response == unknown:
            unknown()
    	else:
    		break

qnada()


