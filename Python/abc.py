try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print(f"{a} / {b} = {result}")
except ValueError:
    print("Hint: Enter valid")   
except ZeroDivisionError:
    print("Hint: Can not divide by 0")
except:
    print("Something wrong, try again.")