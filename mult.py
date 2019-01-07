nb = int(input("\nPlease enter a number:\n(or press [ctrl + C] to quit)\n> "))

def multiplication_table(nb, max = 10):
  i = 0
  while i < max:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1

multiplication_table(nb)