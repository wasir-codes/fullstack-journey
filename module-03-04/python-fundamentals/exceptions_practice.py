class NegativeNumberError(Exception):
    pass

def calculate(user_input):
    try:
        number = int(user_input)
        if number < 0:
            raise NegativeNumberError("Number cannot be negative")
        result = 100 / number
    except ValueError:
        print("It's not a number. Please enter a number")
    except ZeroDivisionError:
        print("Can't be divided by zero")
    except NegativeNumberError as e:
        print(f"Invalid input: {e}")    
    else:
        print("Division worked:", result)
        return result
    finally:
        print("Calculation attempt finished")        

calculate("5")
calculate("abs") 
calculate("0")
calculate("-5")   