import os
import time
text1="""
             _.!._
            /O*@*O\\
           <\@(_)@/>
  ,;,   .--;`     `;--.   ,
  O@O_ /   |d     b|   \ _hnn
  | `/ \   |       |   / \` |
  &&&&  :##;\     /;##;  &&&&
  |  \ / `##/|   |##'  \ /  |
   \   %%%%`       `%%%%   /    
         
     
     HAPPY GANESH CHATURTHI

"""
lines = """
╔═══╦╗──╔╗ ╔═══╦═══╦═══╦╗─╔╦═══╗
║╔═╗║╚╗╔╝║ ║╔═╗║╔═╗║╔═╗║║─║║╔═╗║
║╚══╬╗║║╔╝ ║║─╚╣╚═╝║║─║║║─║║╚═╝║
╚══╗║║╚╝║─ ║║╔═╣╔╗╔╣║─║║║─║║╔══╝
║╚═╝╠╬╗╔╝─ ║╚╩═║║║╚╣╚═╝║╚═╝║║
╚═══╩╝╚╝──•╚═══╩╝╚═╩═══╩═══╩╝
"""

from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
C = Fore.CYAN

def main():
	os.system('clear')
	print(R + text1)
	time.sleep(0.5)
	os.system('clear')
	print(G + text1)
	time.sleep(0.5)
	os.system('clear')
	print(B + text1)
	time.sleep(0.5)
	os.system('clear')
	print(Y + text1)
	time.sleep(0.5)
	os.system('clear')
	os.system('clear')
	print(R + text1)
	time.sleep(0.5)
	os.system('clear')
	print(G + text1)
	time.sleep(0.5)
	os.system('clear')
	print(B + text1)
	time.sleep(0.5)
	os.system('clear')
	print(Y + text1)
	time.sleep(0.5)
	os.system('clear')
	from time import sleep
	import sys
	for line in lines:
	       for c in line:
	       	print(c, end='')
	       	sys.stdout.flush()
	       	sleep(0.01)
	print('')
	time.sleep(5)
	return main()
main()
