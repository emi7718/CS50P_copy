import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('.py'):
    sys.exit('Not a python file')
else:
    try:
        test_file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        test_file.close()

with open(sys.argv[1]) as file:
    text_list = file.readlines()
    code_lines = len(text_list)
    for i in range(len(text_list)):
        if text_list[i].lstrip().startswith('#'):
            code_lines -= 1
        elif text_list[i].isspace():
            code_lines -= 1
    print(code_lines)
