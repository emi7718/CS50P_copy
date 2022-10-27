import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

def printing(f,s):
    figlet.setFont(font=f)
    print('Output:\n', figlet.renderText(s))

list_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    my_string = input('Input: ').strip()
    printing(random.choice(list_fonts), my_string)
elif len(sys.argv) == 3:
    if (sys.argv[1] == '--font' or sys.argv[1] == '-f') and sys.argv[2] in list_fonts:
        my_string = input('Input: ').strip()
        printing(sys.argv[2], my_string)
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')