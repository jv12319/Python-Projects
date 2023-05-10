import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

# Create a connection to the database
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
mycursor = mydb.cursor()

#create a database
#mycursor.execute("CREATE DATABASE Expense_Tracking")

# create a table to store expense information
#mycursor.execute('CREATE TABLE expenses (expense_id INT PRIMARY KEY, amount DECIMAL(10, 2) NOT NULL, date_of_expense DATE NOT NULL, notes_desc VARCHAR(255))')

#Adding additional columns to the table
#mycursor.execute('Alter TABLE expenses ADD COLUMN category VARCHAR(255), ADD COLUMN store_name VARCHAR(255), ADD COLUMN payment_method VARCHAR(255), ADD COLUMN location VARCHAR(255)')


while True:
    #displaying interactive menu for user
    print('Welcome to the Expense Tracker. Please view the following five options.')
    print('1. Add expense')
    print('2. View expenses')
    print('3. Edit expense')
    print('4. Delete expense')
    print('5. Exit')
    choice = input('Enter your choice (1-5): ')

    if choice == '1':
        #add expense
        expense_ID = int(input("Enter the expense id: "))
        amount = float(input("Enter amount: "))
        date_of_expense = input('Enter date of expense (YYYY-MM-DD): ')
        notes_desc = input('Enter notes or description: ')
        category = input('Enter the category of this expense: ')
        store_name = input('Enter the name of the store: ')
        payment_method = input('Enter the payment method used for this expense: ')
        location = input('Enter the location of the store: ')
        

        # insert expense information into expenses table
        sql = 'INSERT INTO expenses (expense_ID, amount, date_of_expense, notes_desc, category, store_name, payment_method, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (expense_ID, amount, date_of_expense, notes_desc, category, store_name, payment_method, location)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'expense added successfully!')

    elif choice == '2':
        #view expense
         mycursor.execute('SELECT * FROM expenses')
         expenses = mycursor.fetchall()

        #print expense records
         for expense in expenses:
            print('Expense ID:', expense[0])
            print('Amount:', expense[1])
            print('Date of Expense:', expense[2])
            print('Notes/Description:', expense[3])
            print('Category:', expense[4])
            print('Store Name:', expense[5])
            print('Payment Method:', expense[6])
            print('Location:', expense[7])
            print('\n')
    
    elif choice == '3':
        expense_id = input('Enter expense ID to edit: ')
        # retrieve expense information for the specified expense ID
        mycursor.execute('SELECT * FROM expenses WHERE expense_id = %s', (expense_id,))
        expense = mycursor.fetchone()

        # check if expense exists for the specified ID
        if expense:
            expense_ID = input('Enter new expense ID: ')
            amount = input('Enter new amount: ')
            date_of_expense = input('Enter new date of expense (YYYY-MM-DD): ')
            notes_desc = input('Enter new notes or description: ')
            category = input('Enter the new category of this expense: ')
            store_name = input('Enter the new name of the store: ')
            payment_method = input('Enter the new payment method used for this expense: ')
            location = input('Enter the new location of the store: ')
            

            # update expense information in the expenses table
            sql = 'UPDATE expenses SET expense_ID = %s, amount = %s, date_of_expense = %s, notes_desc = %s, category = %s, store_name = %s, payment_method = %s, location = %s WHERE expense_id = %s'
            val = (expense_ID, amount, date_of_expense, notes_desc, category, store_name, payment_method, location, expense_id)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, 'expense updated successfully!')
        else:
            print('Expense does not exist for the specified ID.')
    
    elif choice == '4':
        expense_id = input('Enter expense ID to delete: ')
         # delete expense information from the expenses table for the specified expense ID
        sql = 'DELETE FROM expenses WHERE expense_id = %s'
        val = (expense_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'expense deleted successfully!')

    elif choice == '5':
        print('Exiting expense tracker')
        break

    else:
        print('Invalid choice. Please enter a number between 1 and 5.')
    




mydb.commit()
