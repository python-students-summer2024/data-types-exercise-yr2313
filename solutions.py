"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""

def calculate_profit():
  """
  Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales. 
  Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.  
  You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
  The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
  """
  sales = input("Enter total sales: ")
  profit = int(sales) * 0.23
  print("Profit: $" + format(profit, ',.2f'))

def calculate_quotient_and_remainder():
  """
  Complete this function so that it asks the user to input two integers. 
  You program should calculate and output the quotient and remainder when the first number is divided by the second.
  Here's an example run of the function: 
    Enter number #1: 5
    Enter number #2: 2
    "2 goes into 5 a total of 2 times with a remainder of 1"
  """
  num_1 = input("Enter number #1: ")
  num_2 = input("Enter number #2: ")
  num_1 = int(num_1)
  num_2 = int(num_2)
  quotient = num_1 / num_2
  remainder = num_1 % num_2
  message = "{num_2} goes into {num_1} a total of {quotient} times with a remainder of {remainder}".format(num_1=num_1, num_2=num_2, quotient=format(quotient, '.0f'), remainder=remainder)
  print(message)

def calculate_miles_per_gallon():
  """
  A car's Miles Per Gallon (MPG) can be calculated using the following formula: 
    MPG = Miles driven / Gallons of Gas Used
  Complete this function so that it asks the user for the number of miles driven and the gallons of gas used. 
  It should calculate the car's MPG and display the result in the format:
    "Miles per gallon: 2.2"
  """
  miles = input("Miles driven: ")
  gas = input("Gallons of gas used: ")
  miles = int(miles)
  gas = int(gas)
  mpg = miles / gas
  print("Miles per gallon: {}".format(mpg))

def align_text():
  """
  Complete this function such that it asks the user to enter in 3 price values (as floating point numbers). 
  The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
  Here's a sample running of the program:

    Enter price #1: 1.55
    Enter price #2: 10
    Enter price #3: 9532.6

    Here are your prices!

    Price #1: $    1.55
    Price #2: $   10.00
    Price #3: $ 9532.60
  """
  price_1 = input("Enter price #1: ")
  price_2 = input("Enter price #2: ")
  price_3 = input("Enter price #3: ")
  price_1 = float(price_1)
  price_2 = float(price_2)
  price_3 = float(price_3)
  print("Here are your prices!")
  print()
  print("Price #1: $" + format(price_1, ">8.2f"))
  print("Price #2: $" + format(price_2, ">8.2f"))
  print("Price #3: $" + format(price_3, ">8.2f"))
