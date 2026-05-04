import os
from datetime import date

# HR can do everything,
# wasn't sure if manager should be allowed to view salaries

def check_digits(*any_value):
    return all(str(value).isdigit() for value in any_value)

# funtion to calculate salaries
def salary_workers():    #for full-time employees
 if employee_type in ["full-time", "f", "full"]:
  gross_salary = base_salary + allowance
  if gross_salary > 3000:
    difference = gross_salary - 3000
    tax = ((difference / 100) * 15) # 15% tax on amount over 3000
    net_salary = gross_salary - tax - deduction
  else:
    net_salary = gross_salary - deduction  # no tax (under 3000)

# part-time employees, this function is only called
# when HR wants to add a new record, so i didnt specify in the code that its part-time
 else:
  gross_salary = (hourly_rate * hours_worked) + allowance
  if gross_salary > 2000:
    difference = gross_salary - 2000
    tax = ((difference / 100) * 10) # 10% tax on amount over 2000
    net_salary = gross_salary - tax - deduction
  else:
    net_salary = gross_salary - deduction # no tax
 return net_salary

# this function is for adding new employee records
def get_reports():
  current_date = date.today().strftime("%d-%m-%y")
  with open("salaries.txt", "a") as salary_reports:
    salary_reports.write(f"\n{name_employee} -- {employee_type} -- {final_salary:.2f} -- {current_date}")

# if the file doesnt exist or if its empty, this wil add the header.
# meaning the header will appear one time at the top and not be duplicated.

if not os.path.exists("salaries.txt") or os.stat("salaries.txt").st_size == 0:
  with open("salaries.txt", "w") as salary_reports:
    salary_reports.write(f"           |   EMPLOYEE RECORDS   | ")

# name and role assignment
name = input("What is your name? ").title()
while True:
 role = input("Are you HR, a Manager or an Employee?: ").lower()
 match role:
    case "hr":
      print(f"Hello {name}, you have the role of {role.upper()}")
      break
    case "manager":
      print(f"Hello {name}, you have the role of {role.capitalize()}")
      answer = input("Would you like to view the salary reports?\nType view, to exit type anything else: ")
      if answer == "view":
        with open("EmployeeSalaries.txt") as salary_reports:
          print(salary_reports.read())
          break
      else:
        break
    case "employee":
      print(f"Hello {name}, you have the role of {role.capitalize()}")
      break
    case _:
      print(f"Please enter a valid role, {name}")

while role == "hr":
 answer = input(f"\n{name}, would you like to:\nView the salary records\nAdd a new employee record\nDelete an existing record\nType view, add, d to delete. To exit, enter any key: ").lower()

 if answer == "add":
  name_employee = input("Enter the full name of the employee to proceed or enter q to return: ").title()
  if name_employee == "Q":
    continue
  else:
   while True:
    employee_type = input(f"is {name_employee} working full-time or part-time?\nEnter f or p: ").lower()
    match employee_type:
     case "full-time" | "fulltime" | "f":
       employee_type = "full-time"
       while True: # Loop for full-time input validation
           base_salary_str = input(f"What is {name_employee}'s monthy salary? $")
           allowance_str = input(f"How much is {name_employee}'s allowance? $")
           deduction_str = input(f"How much is going to be deducted? $")
           if check_digits(base_salary_str, allowance_str, deduction_str):
               base_salary = float(base_salary_str)
               allowance = float(allowance_str)
               deduction = float(deduction_str)
               break
           else:
               print("Please enter numbers.")
       break

     case "part-time" | "parttime" | "p":
       employee_type = "part-time"
       while True: # Loop for part-time input validation
         hourly_rate_str = input(f"What is {name_employee}'s hourly rate? $")
         hours_worked_str = input(f"How many hours did {name_employee} work?: ")
         allowance_str = input(f"How much is {name_employee}'s allowance? $")
         deduction_str = input(f"How much is going to be deducted? $")
         if check_digits(hourly_rate_str, hours_worked_str, allowance_str, deduction_str):
          hourly_rate = float(hourly_rate_str)
          hours_worked = float(hours_worked_str)
          allowance = float(allowance_str)
          deduction = float(deduction_str)
          if hours_worked > 160:
            hours_worked = 160
            print("Employees can only work a maximum of 160 hours per month! Hours worked capped at 160.")
          break
         else:
          print("Please enter numbers.")
          continue
       break
     case _:
        print("Please enter either full-time or part-time!")
        continue

   final_salary = (salary_workers())
   print(f"\n{name_employee}'s net salary is ${final_salary}")
   get_reports()

 elif answer == "view":
  with open("salaries.txt") as salary_reports:
   print(salary_reports.read())

 elif answer == "d":
  redacted_name = input("\nEnter the full name of which employee you'd like to delete or any q to return: ").title()
  if redacted_name == "Q":
    continue
  with open("salaries.txt" , "r+") as salary_reports:
    new_report = salary_reports.readlines()
    salary_reports.seek(0)
    for line in new_report:
      if redacted_name not in line:
        salary_reports.write(line)
    salary_reports.truncate()
    print(f"Record succesfully removed from the report!")
  # this opens the file and stores the lines in a list
  # after going through every line, it goes back to the start of the file
  # if the name isn't in a line, that line is written again (instead of removed)
  # when it finds the name, whole line is removed.

 else:
    break
