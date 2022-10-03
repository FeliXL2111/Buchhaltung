def comparison(date1, date2):
    date1 = date1.split('_')
    for number in date1:
        int(number)
    date2 = date2.split('_')

    day = 0
    
    month = 1
    
    year = 2
    

    if date1[year] > date2[year]:
        return 'first later'
    elif date1[year] == date2[year]:

        if date1[month] > date2[month]:
            return 'first later'
        elif date1[month] == date2[month]:

            if date1[day] > date2[day]:
                return 'first later'
            elif date1[day] == date2[day]:
                return 'eqaul'
            else:
                return 'first earlyer'

        else:
            return 'first earlyer'
        
    else:
        return 'first earlyer'
    

print(comparison('02_11_2017', '02_11_2021'))