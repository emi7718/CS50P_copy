def main():
    time = input('Enter the time of day: ')
    if time.endswith(' a.m.'):
        time = time.rstrip(' a.m.')
        time = convert(time)
        #print(type(time))
        if 7 <= time <= 8:
           print('Breakfast time')
        elif 12 <= time < 13:
            print('Lunch time')
    elif time.endswith(' p.m.'):
        time = time.rstrip(' p.m.')
        time = convert(time)
        if 6 <= time <= 7 :
            print('Dinner time')
        elif time == 1:
            print('Lunch time')
    else:
        time = convert(time)
        if 8 >= time >= 7:
            print('Breakfast time')
        elif 13 >= time >= 12:
            print('Lunch time')
        elif 19 >= time >= 18:
            print('Dinner time')

def convert(time):
    hours , minutes = time.split(':')
    int_var = float(hours) + (float(minutes) / 60)
    return int_var
main()