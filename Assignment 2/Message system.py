Message= input("Enter Your Request: ")
Hours= input("How Many Hours Has The Ticket Been Opean?: ")

Hours= float(Hours)
print(type(Hours))

if "payment" in Message:

    Team = "Billing"

elif "delivery" in Message:

    Team = "Logistics"

elif "error" in Message:

    Team = "Tech"

else:

    Team = "Gneral"

if Hours >= 24:

    Priority = "High"
else:

    Priority = "Normal"

print("Team: ", Team) 
print("Priority: ", Priority) 