Chapter_3 = "Conditional Execution"

def exercise_1():
    hours = None
    rate = None
    
    try:
        working_hours = input("How many hours do you work: ")
        hours = float(working_hours)
        print(f"You work: {working_hours} hours")
        hourly_rate = input("What is your hourly rate: ")
        rate = float(hourly_rate)
        print(f"Your current hourly rate is: ${rate}")
        pay = hours * rate
        print(f"Your gross paycheck for this pay period is: ${pay}")
        print(f"Should your job round to the nearest dollar your pay is now: ${round(pay)}")
    
    except:
        print("Incorrect value entered.")
        return
#exercise_1()