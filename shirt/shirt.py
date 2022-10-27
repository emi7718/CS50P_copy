from PIL import Image, ImageOps
import sys
import os

extensions_list = ['.jpg', '.jpeg', '.png']

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if '.' in sys.argv[1] and '.' in sys.argv[2]:
    trash, inpt_ext = os.path.splitext(sys.argv[1])
    trash, outpt_ext = os.path.splitext(sys.argv[2])
    inpt_ext = inpt_ext.lower()
    outpt_ext = outpt_ext.lower()
    if inpt_ext not in extensions_list:
        print(inpt_ext)
        sys.exit('Invalid input')
    if outpt_ext not in extensions_list:
        sys.exit('Invalid output')
    elif inpt_ext != outpt_ext:
        sys.exit('Input and output have different extensions')
#else:
 #   sys.exit('blabla')

try:
    im = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit('Input does not exist')
else:
    portrait = ImageOps.fit(im , size=(600,600))
    shirt = Image.open('shirt.png')
    portrait.paste(shirt, shirt)
    portrait.save(f'{sys.argv[2]}')
