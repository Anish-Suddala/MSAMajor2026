def float_in_hours():
    while(True):
        try:
            number_of_hours = float(input("Enter the number of hours worked daily: "))
            if number_of_hours>24:
                print("Error: Cannot work for more than 24 hours")
                continue
            break
        except:
            print("Error: Please enter a number.\n")
            continue
    return number_of_hours

def float_in_wage():
    while(True):
        try:
            hourly_wage = float(input("Enter the hourly wage: "))
            if hourly_wage<0:
                print("Error: Please enter a positive number")
                continue
            break
        except:
            print("Error: Please enter a number.\n")
    return hourly_wage

def main():
    number_of_hours = float_in_hours()
    hourly_wage = float_in_wage()
    wage_before_taxes = hourly_wage*350*number_of_hours
    tax_amount = wage_before_taxes*0.12
    annual_wage_after_taxes = wage_before_taxes-tax_amount
    print("Pay Advice \n")
    print("--------------\n")
    print(f"Hours Worked: {number_of_hours:.2f}\n")
    print(f"Hourly Wage: ${hourly_wage:.2f}\n")
    print(f"Wages Before Taxes: ${wage_before_taxes:.2f}\n")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Annual Wage After Taxes: ${annual_wage_after_taxes:.2f}")
main()
