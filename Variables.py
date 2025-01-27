def flooring_test():
    minute = 59
    minute1 = minute/60
    print(minute1)
    minute2 = minute//60
    print(minute2)

#flooring_test()

def remainder_test():
    division = 7 / 3
    print(f"total sum: {division:.2f}")
    
    qoutient = 7 // 3
    print(f"qoutient: {qoutient}")
    
    remainder = 7 % 3
    print(f"remainder: {remainder}")

#remainder_test() 

def type_conversion():
    x = 2.323
    print(type(x))
    y = 23
    print(f"Testing variable y: y = {y} {type(y)}")
    print(f"Updated value after convered to a float: {float(y)}")

#type_conversion()

def exercise_2():
    name = input("what is your name?\n")
    print(f"Hello {name}")

#exercise_2()

def exercise_3():
    hours = None
    rate = None
    working_hours = input("How many hours do you work: ")
    hours = int(working_hours)
    print(f"You work: {working_hours} hours")
    hourly_rate = input("What is your hourly rate: ")
    rate = float(hourly_rate)
    print(f"Your current hourly rate is: ${rate}")
    pay = hours * rate
    print(f"Your gross paycheck for this pay period is: ${pay}")
    print(f"Should your job round to the nearest dollar your pay is now: ${round(pay)}")

#exercise_3()

def temp_conversion():
    celsius = None
    fahrenheit = None
    ask_temp_type = input("Would you like to convert to Celsius (C) or Fahrenheit (F)? ")

    if ask_temp_type in ["C", "c"]:
        temp = float(input("You have selected Celsius conversion. Please enter the temperature in Fahrenheit: "))
        print(f"The temperature you entered is {temp}°F")
        celsius = (temp - 32) * (5 / 9)
        print(f"The converted temperature is: {celsius:.2f}°C")

    elif ask_temp_type in ["F", "f"]:
        temp = float(input("You have selected Fahrenheit conversion. Please enter the temperature in Celsius: "))
        print(f"The temperature you entered is {temp}°C")
        fahrenheit = (temp * (9 / 5)) + 32
        print(f"The converted temperature is: {fahrenheit:.2f}°F")

    else:
        print("Invalid input. Please select either 'C' or 'F'.")


#temp_conversion()
