import re

def main():
    print(parse(input('HTML: ')))

def parse(s):
    
    if (match := re.search(r'src="https?://(www\.)?youtube\.com/embed/(\w+)"', s)):
        return ('https://youtu.be/' + match.group(2))
    return None
        

if __name__ == '__main__':
    main()

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0