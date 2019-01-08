def leap_year():
  while True:
    year = input('\nPlease enter a year superior than 0:\n(or press [ctrl + C] to quit)\n> ')
    try:
      year = int(year)
      assert year > 0
    except ValueError:
      print("You did not enter a number.")
      leap_year()
    except AssertionError:
      print("The year entered is less than or equal to 0.")
      leap_year()

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
      print('The year %d is a leap year.' %(year))
    else:
      print('The year %d is not a leap year.' %(year))

leap_year()