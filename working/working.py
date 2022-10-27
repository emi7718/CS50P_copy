import re

def main():
    print(convert(input('Hours: ')))


def convert(s):
    finishing_hour = str()
    beginning_hour = str()
    if match := re.search(r'^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$', s):
        #from here we calculate starting hour
        if match.group(3) == 'AM':
            if int(match.group(1)) < 12:
                if match.group(2):
                    beginning_hour = f'{int(match.group(1)):02}:{int(match.group(2)):02}'
                else:
                    beginning_hour = f'{int(match.group(1)):02}:00'
            else:
                if match.group(2):
                    beginning_hour = f'00:{int(match.group(2)):02}'
                else:
                    beginning_hour = '00:00'
        else:
            if int(match.group(1)) < 12:
                if match.group(2):
                    beginning_hour = f'{(int(match.group(1)) + 12):02}:{int(match.group(2)):02}'
                else:
                    beginning_hour = f'{(int(match.group(1)) + 12):02}:00'
            else:
                if match.group(1):
                    beginning_hour = f'12:{int(match.group(2)):02}'
                else:
                    beginning_hour = '12:00'

        #from here we calculate finishing hour
        if match.group(6) == 'AM':
            if int(match.group(4)) < 12:
                if match.group(5):
                    finishing_hour = f'{(int(match.group(4))):02}:{int(match.group(5)):02}'
                else:
                    finishing_hour = f'{(int(match.group(4))):02}:00'
            else:
                if match.group(5):
                    finishing_hour = f'00:{int(match.group(5)):02}'
                else:
                    finishing_hour = '00:00'
        else:
            if int(match.group(4)) < 12:
                if match.group(5):
                    finishing_hour = f'{(int(match.group(4)) + 12):02}:{int(match.group(5)):02}'
                else:
                    finishing_hour = f'{(int(match.group(4)) + 12):02}:00'
            else:
                if match.group(5):
                    finishing_hour = f'12:{int(match.group(5)):02}'
                else:
                    finishing_hour = '12:00'

        return f'{beginning_hour} to {finishing_hour}'
    else:
        raise ValueError

if __name__ == '__main__':
    main()
