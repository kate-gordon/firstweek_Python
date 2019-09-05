amt_of_bill = float(input("Total bill amount? "))
rank_service = input("Good, Fair, or Bad Service? ")
split_amt = int(input("Split how many ways? "))

def tip(rank_service): 
    if rank_service == "Good":
        return amt_of_bill * .2
    elif rank_service == "Fair":
        return amt_of_bill * .15
    elif rank_service == "Bad": 
        return amt_of_bill * .10

print ("Tip Amount: " + str(tip(rank_service)))
total = tip(rank_service) + amt_of_bill
print ("Total amount: " + str(total))
print ("Amount per person: " + str(total/split_amt))



