while True:
  year = int(input('\nPlease enter a year:\n(or press [ctrl + C] to quit)\n> '))

  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('The year %d is a leap year.' %(year))
  else:
    print('The year %d is not a leap year.' %(year))