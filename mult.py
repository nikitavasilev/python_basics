"""multiplication table module"""

def multiplication_table():
  while True:
    nb = input("\nPlease enter a number:\n> ")
    try:
      nb = int(nb)
    except ValueError:
      print('The value must be an integer.')
      multiplication_table()
    else:
      print("There is the multiplication table of " + str(nb) + ":\n")

    def perform(nb, max = 10):
      i = 0
      while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

    perform(nb)
    input("\nPress enter to continue, or press [ctrl + C] to quit.")

if __name__ == "__main__":
  multiplication_table()