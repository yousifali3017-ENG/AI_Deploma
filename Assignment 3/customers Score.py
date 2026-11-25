Customers = ["Ahmed", "Sara", "Omar", "Mona","Ali", "Nour", "Youssef", "Hana","Khaled", "Mariam", "Hassan", "Laila"]

Scores = [91, 45, 78, 66, 88, 30, 72, 95, 51, 60, 84, 39]

Risk_Levels = []

High = 0
Medium = 0
Low = 0
Total = 0
for customer, score in zip(Customers,Scores):
    if score >= 85:
        Risk = "High"
        High += 1
    elif 60 <= score < 85:
        Risk = "Medium"
        Medium += 1
    else:
        Risk = "Low"
        Low += 1
    
    Risk_Levels.append(Risk)
    Total += score

Average = Total / 12

Best_Customer = Customers[0]
Best_Score = Scores[0]
Worst_Customer = Customers[0]
Worst_Score = Scores[0]

for customer, score in zip(Customers, Scores):
    if score < Best_Score:
        Best_Score = score
        Best_Customer = customer

    if score > Worst_Score:
        Worst_Score = score
        Worst_Customer = customer

while True:
    print()
    print("========== MENU ==========")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("0. Exit")
    print("============================")

    Choice = input("Enter your choice: ")

    if Choice == "1":
        print()
        print("========== CUSTOMER RISK REPORT ==========")
        print(f"{'Name':<10} {'Score':<6} {'Risk'}")
        print("-" * 26)
        for customer, Score, Risk in zip(Customers, Scores, Risk_Levels):
            print(f"{customer:<10} {Score:<6} {Risk}")
        
        print("\n============== SUMMARY ==============")
        print(f"High Risk: {High}")
        print(f"Medium Risk: {Medium}")
        print(f"Low Risk: {Low}")
        print(f"Average Score: {Average:.2f}\n")
        print(f"Best Customer: {Best_Customer} ({Best_Score})")
        print(f"Worst Customer: {Worst_Customer} ({Worst_Score})")
        

    elif Choice == "2":
        Search_Name = input("Enter customer name: ")

        for customer, score, Risk in zip(Customers, Scores, Risk_Levels):
            if customer == Search_Name:
                print("Name:", customer)
                print("Score:", score)
                print("Risk:", Risk)
                break

        if customer != Search_Name :
            print("Customer not found")
                
       
    elif Choice == "0":
            print("Goodbye")
            break

    else:
        print("Wrong Choice")