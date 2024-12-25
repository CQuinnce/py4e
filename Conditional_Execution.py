Chapter_3 = "Conditional Execution"

def tesing_comparison_operators():
    x = 3
    if x < 10:
        print("small")

    print("fucntion done")

#tesing_comparison_operators()

def exercise_1_2():
    hours = None
    rate = None
    
    try:
        working_hours = input("How many hours do you work: ")
        hours = float(working_hours)
        print(f"You work: {working_hours} hours")
        
        hourly_rate = input("What is your hourly rate: ")
        rate = float(hourly_rate)
        print(f"Your current hourly rate is: ${rate}")
        
        if hours <= 40:
            pay = hours * rate
            print(f"Your gross paycheck for this pay period is: ${pay}")

        elif hours > 40:
            overtime = hours - 40
            ot_pay = (hours * rate) + (overtime * (rate * 1.5))
            print(f"You have {overtime} hours of overtime")
            print(f"Your gross paycheck for this pay period is: ${ot_pay}")
        #print(f"Should your job round to the nearest dollar your pay is now: ${round(pay)}")
    
    except ValueError:
        print("Incorrect value entered.")
        return
#exercise_1_2()

def exercise_3():
    grade = input("Please enter your grade: ")
    grade = float(grade)
    if grade > 1 or grade < 0:
        print("Invalid input, try again.")
        return
    grade_percentage = [(1,"A"),(.89, "B"),(.79, "C"),(.69, "D"),(.59, "F")]
    if grade >= .9:
        print("Your grade is A.")
    elif grade >= .8:
        print("Your grade is B.")
    elif grade >= .7:
        print("Your grade is C.")
    elif grade >= .6:
        print("Your grade is D.")
    else:
        print("Your grade is F.")
#exercise_3()

def exercise_3py():
    grade = input("Please enter your grade: ")
    try:
        grade = float(grade)
        if grade > 1 or grade < 0:
            print("Invalid input, try again.")
            return
        # Simplified grade thresholds (only lower bounds)
        grade_percentage = [("A", 0.9), ("B", 0.8),
                            ("C", 0.7), ("D", 0.6), ("F", 0)]

        # Iterate through the grades and find the first matching threshold
        for letter, threshold in grade_percentage:
            if grade >= threshold:
                print(f"Your grade is {letter}.")
                return
    except ValueError:
        print("Please enter a numeric value.")


exercise_3py()
