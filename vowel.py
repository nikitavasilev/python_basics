while True:
  string = input("\nPlease type a string:\n(or press [ctrl + C] to quit)\n> ")
  for character in string:
    if character in "AEIOUYaeiouy":
      print(character, 'is a vowel.')
    else:
      print(character, 'is not a vowel.')