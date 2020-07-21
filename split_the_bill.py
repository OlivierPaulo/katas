def split_the_bill(expenses):
    # Good Luck!
    mean = round(sum(expenses.values())/len(expenses),2)    #Calculate mean of expenses of the group
    for person, amount in expenses.items():                 #Looping trough expenses
        expenses[person] = round(amount-mean,2)             #Calculate, round and store difference between amount and mean 
    return expenses                                         #Returning the expenses new dict
