months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convert_list_to_int(list_to_convert):
    for i in range(len(list_to_convert)):
        list_to_convert[i] = int(list_to_convert[i])
    return list_to_convert

def check_day_month(list_to_check):
        if 0 < int(list_to_check[0]) < 13:
            if 0 < int(list_to_check[1]) < 32:
                return True
        else:
            raise ValueError


while True:
    try:
        date = input('Date: ').strip()
        if date.count(',') == 1:
            list1 = date.split(',')
            list2 = list1[0].split(' ')
            list_final = [list2[0].strip(), list2[1].strip(), list1[1].strip()]
            if list_final[0] in months_list:
                list_final[0] = str(months_list.index(list_final[0]) + 1)
                if check_day_month(list_final):
                    list_final = convert_list_to_int(list_final)
                    print(f'{list_final[2]}-{list_final[0]:02}-{list_final[1]:02}')
                    break
        elif date.count('/') == 2:
            list_final = date.split('/')
            for i in range(len(list_final)):
                list_final[i] = list_final[i].strip()
            if check_day_month(list_final):
                list_final = convert_list_to_int(list_final)
                print(f'{list_final[2]}-{list_final[0]:02}-{list_final[1]:02}')
                break


    except ValueError:
        pass


