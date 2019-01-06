year = int(input('Please enter a year:\n> '))
leap_year = False

if (year % 400 == 0):
  leap_year = True
elif (year % 100 == 0):
  leap_year = False
elif (year % 4 == 0):
  leap_year = True
else:
  leap_year = False


if (leap_year == True):
  print('The year %d is a leap year.' %(year))
else:
  print('The year %d is not a leap year.' %(year))