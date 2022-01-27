# programme qui permet de suprimer les transactions double

transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]

resultanttransaction_list= []

for element in transaction_list:
    
    if element not in resultanttransaction_list:
        
        resultanttransaction_list.append(element)

print(resultanttransaction_list)