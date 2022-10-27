def convert(sentence):
    if ':)' in sentence or ':(' in sentence:
        sentence = sentence.replace(':)','🙂')
        sentence = sentence.replace(':(','🙁')
    return sentence
def main():
    phrase = input('Please enter your sentence:\n')
    print(convert(phrase))


main()
