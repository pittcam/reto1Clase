import math

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

# Main program
limit = 4000000
result = problem_2(limit)
print("The sum of even-valued terms in the Fibonacci sequence up to", limit, "is:", result)


def problem_1(limit):
  """
  Calculate the sum of all multiples of 3 or 5 below the given limit.
  """
  total_sum = 0
  for i in range(limit):
      if i % 3 == 0 or i % 5 == 0:
          total_sum += i
  return total_sum

# Main program
limit = 1000
result = problem_1(limit)
print("The sum of all multiples of 3 or 5 below", limit, "is:", result)

def problem_4(n):
  """
  Check if a number is a palindrome.
  """
  return str(n) == str(n)[::-1]

def largest_palindrome_product():
  """
  Find the largest palindrome made from the product of two 2-digit numbers.
  """
  max_palindrome = 0
  for i in range(10, 100):
      for j in range(10, 100):
          product = i * j
          if problem_4(product) and product > max_palindrome:
              max_palindrome = product
  return max_palindrome

# Main program
largest = largest_palindrome_product()
print("The largest palindrome made from the product of two 2-digit numbers is:", largest)

def problem_3(number):
  """
  Find the largest prime factor of the given number.
  """
  # Inicializamos el factor primo más grande como 1
  largest_factor = 1
  # Inicializamos el divisor como 2
  divisor = 2

  # Mientras el número sea mayor que 1
  while number > 1:
      # Si el número es divisible por el divisor actual
      if number % divisor == 0:
          # El divisor actual es un factor primo
          largest_factor = divisor
          # Dividimos el número por el divisor actual
          number //= divisor
      else:
          # Si no es divisible, incrementamos el divisor
          divisor += 1
  return largest_factor

# Número dado
number = 600851475143
# Calculamos el mayor factor primo
result = problem_3(number)
print("El factor primo más grande del número", number, "es:", result)


def gcd(a, b):
    """
    Calcular el mínimo común múltiplo (LCM) de dos números.
    """
    return (a * b) // gcd(a, b)

def problem_5(n):
    """
    Encontrar el número más pequeño divisible por todos los números del 1 al n.
    """
    result = 1
    for i in range(2, n + 1):
        result = gcd(result, i)
    return result

# Main program
limit = 20
result = problem_5(limit)
print("El número más pequeño divisible por todos los números del 1 al", limit, "es:", result)
