from math import gcd

# Problem 1 
def problem_1(limit):
  """
  Calculate the sum of all multiples of 3 or 5 below the given limit.
  """
  total_sum = 0
  for i in range(limit):
      if i % 3 == 0 or i % 5 == 0:
          total_sum += i
  return total_sum

# Problem2
def problem_2(limit):
  """
  Calculate the sum of even-valued terms in the Fibonacci sequence up to the given limit.
  """
  fib_sum = 0
  a, b = 1, 2
  while a <= limit:
      if a % 2 == 0:
          fib_sum += a
      a, b = b, a + b
  return fib_sum


# Problem3
def problem_3(number):
  """
  Find the largest prime factor of the given number.
  """
  # the largest prime factor is initialized as 1
  largest_factor = 1
  # the divisor is initialized as 2
  divisor = 2

  # As long as the number is greater than 1
  while number > 1:
      # If the number is divisible by the current divisor
      if number % divisor == 0:
          # The current divisor is a prime factor
          largest_factor = divisor
          # Divide the number by the current divisor
          number //= divisor
      else:
          # If it is not divisible, to increase the divisor
          divisor += 1
  return largest_factor

# Problem_4
def problem_4():
  max_palindromo = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      if str(product) == str(product)[::-1] and product > max_palindromo:
        max_palindromo = product
  return max_palindromo

# Problem_5
def lcm(a, b):
    """
    Calculate the least common multiple (LCM) of two numbers.
    """
    return (a * b) // gcd(a, b)

def problem_5(n):
    """
    Find the smallest number divisible by all the numbers from 1 to n.
    """
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result
