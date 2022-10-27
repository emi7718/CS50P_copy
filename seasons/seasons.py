import datetime
import sys, inflect

def main():

    print(convert_num_to_letter(input('Date of birth: ')))

def convert_num_to_letter(s):
    try:
        birth_year, birth_month, birth_day= s.split('-')
        birth_data = datetime.date(int(birth_year), int(birth_month) ,int(birth_day))
    except ValueError:
        sys.exit('Invalid date')
    p = inflect.engine()
    answer = (datetime.date.today() - birth_data)
    return (p.number_to_words(round(answer.days *24 * 60)) + ' minutes').replace(' and', '').capitalize()

if __name__ == '__main__':
    main()
