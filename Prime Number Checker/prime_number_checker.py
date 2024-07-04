def prime_checker(number):
  divisible = False
  for x in range (2, number):
      if (number % x) == 0:
        divisible = True

  if divisible:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)
