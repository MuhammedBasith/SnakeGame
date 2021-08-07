
stock = {'Ford': 10,
         'Mitsubishi': 20,
         'Nissan': 6,
         'Lamborghini': 3,
         'Benz': 8,
         'Toyota': 40,
         'Dodge': 37}


wanted_car = input('Please enter the company name: ').title()

check = stock.get(wanted_car)

if check is None:
    print(f'Sorry! There\'s no more of {wanted_car.title()} left.')
else:
    print(f'There are only {check} {wanted_car} cars left! Hurry up!!')
    y_n = input('Do you want to purchase a car: ')
    if y_n == 'yes':
        stock[wanted_car.title()] = check - 1
        print(stock)
    else:
        print('Bye!')
