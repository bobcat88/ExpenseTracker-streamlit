expenses = []
#incomes = []
expense1= {'amount': '32.00', 'category': 'Online shopping'} #testing value
expenses.append(expense1) #testing value
expense2= {'amount': '58.25', 'category': 'Amazon'} #testing value
expenses.append(expense2) #testing value

def invalidValue():
    print("Invalid input, please try again.")

def removeExpense():
    while True:
        listExpenses()
        print("what expense would you like to remove ?")
        try:
            expenseToRemove = int(input('>'))
            expenses.remove[expenseToRemove]
            break
        except:
            print(invalidValue)

def addExpense (amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

#def addIncome ( amount, category):
#    incomes = {'amount': amount, 'category': category}
#    incomes.append(income)
    
#def sumOfExpenses(): 
#    sumOfExpense = sum(expenses.values())
#    print("Total expenses :", sumOfExpense) 

def printMenu ():
    print("Please choose one of the option...")
    print("1.Add a new expense")
    print("2.Remove an Expense")
    #print('3.Add a source of income')
    print("4.List all")
    
def listExpenses():
    print ('\nHere are all your expenses so far...')
    print ('--------------------------------------')
    counter = 0
    for expense in expenses:
        print('#', counter, '-', expense['amount'], ' - ', expense['category'])
        counter += 1
#   print ('--------------------------------------')
#   print(sumOfExpenses)
    print('\n\n')

if __name__ == "__main__":
    while True:
        #prompt user
        printMenu()
        optionSelected = input('>')

        if (optionSelected == '1'):
            print('How much was this expense?')
            while True :
                try:
                    amountToAdd = input(">")
                    break
                except:
                    print(invalidValue, 'Exemple : 300')

            print('What category was this expense?')
            while True :
                try:
                    category = input(">")
                    break
                except:
                    print(invalidValue,'Exemple : Groceries')
            
            addExpense(amountToAdd, category)
        elif (optionSelected == '2'):
            removeExpense()
        elif (optionSelected == '4'):
            listExpenses()    
        else:
            print(invalidValue)   