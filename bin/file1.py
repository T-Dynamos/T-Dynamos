try:
	from colorama import Fore,Back,Style
except Exception:
	import os
	os.system('pip install colorama')
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y  = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
print(Style.BRIGHT)
cra = """
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
       *
        *"""
cra1 = """
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
                        *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      
  .                  \      |   \          /               
        *     '      \      \   '.       |
        -._            `                  /         
  ' '      ``._   *                           '          .      '
               *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '

    
             """
cra2 = """
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '
"""
diwali = f"""{C}╭╮╱╭┳━━━┳━━━┳━━━┳╮╱╱╭╮ ╭━━━┳━━┳╮╭╮╭┳━━━┳╮╱╱╭━━╮
┃┃╱┃┃╭━╮┃╭━╮┃╭━╮┃╰╮╭╯┃ ╰╮╭╮┣┫┣┫┃┃┃┃┃╭━╮┃┃╱╱╰┫┣╯
┃╰━╯┃┃╱┃┃╰━╯┃╰━╯┣╮╰╯╭╯  ┃┃┃┃┃┃┃┃┃┃┃┃┃╱┃┃┃╱╱╱┃┃
┃╭━╮┃╰━╯┃╭━━┫╭━━╯╰╮╭╯╱  ┃┃┃┃┃┃┃╰╯╰╯┃╰━╯┃┃╱╭╮┃┃
┃┃╱┃┃╭━╮┃┃╱╱┃┃╱╱╱╱┃┃╱╱ ╭╯╰╯┣┫┣╋╮╭╮╭┫╭━╮┃╰━╯┣┫┣╮
╰╯╱╰┻╯╱╰┻╯╱╱╰╯╱╱╱╱╰╯╱╱ ╰━━━┻━━╯╰╯╰╯╰╯╱╰┻━━━┻━━╯
      {G} From noobhackers.com
"""
import os
import time

def main():
	os.system('clear')
	print(R + cra1)
	time.sleep(0.5)
	os.system('clear')
	print(G + cra2)
	time.sleep(0.5)
	os.system('clear')
	print(B + cra1)
	time.sleep(0.5)
	os.system('clear')
	print(Y + cra2)
	time.sleep(0.5)
	os.system('clear')
	os.system('clear')
	print(R + cra1)
	time.sleep(0.5)
	os.system('clear')
	print(G + cra2)
	time.sleep(0.5)
	os.system('clear')
	print(B + cra1)
	time.sleep(0.5)
	os.system('clear')
	print(Y + cra2)
	time.sleep(0.5)
	os.system('clear')
	from time import sleep
	import sys
	print(Y+cra.center(24))
	for line in diwali:
	       for c in line:
	       	print(c, end='')
	       	sys.stdout.flush()
	       	sleep(0.01)
	       	
	print('')
	time.sleep(5)
	return main()
main()
