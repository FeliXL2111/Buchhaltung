def comparison(date1, date2):
    date1 = date1.split('_')
    date2 = date2.split('_')
    for i in range(0, len(date1)):
        date1[i] = int(date1[i])
    for i in range(0, len(date2)):
        date2[i] = int(date2[i])

    print(date1, date2)
    
    day = 0
    month = 1
    year = 2
    

    if date1[year] > date2[year]:
        return 'first closer to today, year'
    elif date1[year] == date2[year]:

        if date1[month] > date2[month]:
            return 'first closer to today, month'
        elif date1[month] == date2[month]:

            if date1[day] > date2[day]:
                return 'first closer to today, day'
            elif date1[day] == date2[day]:
                return 'eqaul'
            else:
                return 'second closer to today, day'

        else:
            return 'second closer to today, month'
        
    else:
        return 'second closer to today, year'
