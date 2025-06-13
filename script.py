# Author: Vernell Mangum
#
# Description: You are a physics teacher preparing for the upcoming semester. 
# You want to provide your students with some functions that will help them calculate some fundamental physical properties.

# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1

# A function that converts Fahrenheit to Celsius 
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5/9)
    
    return c_temp

# Testing 'f_to_c' function
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# A function the converts Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    
    return f_temp

# Testing 'c_to_f' function
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

