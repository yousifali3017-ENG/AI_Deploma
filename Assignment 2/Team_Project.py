Members= input("Enter your team members number: ")
Months= input("Enter the number of monthes the project will take: ")
Salary= input("Enter the salary of each member in the month: ")
Cloud_Cost= input("Enter total cloud cost for the whole project: ")

Members= int(Members)
print(type(Members))
Months= float(Months)
print(type(Months))
Salary= float(Salary)
print(type(Salary))
Cloud_Cost= float(Cloud_Cost)
print(type(Cloud_Cost))

Total_Salary= Members * Months * Salary

Subtotal= Total_Salary + Cloud_Cost

VAT= Subtotal * 0.14

Total= Subtotal + VAT

print(f"Members NUmber: {Members} , Project Time: {Months:,.2f} , Member's Salary in month: {Salary:,.2f} Months , Cloud cost Of The Project: {Cloud_Cost:,.2f} , Total Salary Of All Members: {Total_Salary:,.2f} , Subtotal Of The Project: {Subtotal:,.2f} , Total Money Spent: {Total:,.2f}")