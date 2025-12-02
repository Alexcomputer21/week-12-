# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperature = int(input("What is today's temperature: "))
if temperature < -10 or temperature > 110:
    print("Extreme temperature warning!")
elif -9 <= temperature <= 60:
    print("It's cold")
elif 61 <= temperature <= 90:
    print("It's warm")
elif 91 <= temperature <=109:
    print("It's hot")