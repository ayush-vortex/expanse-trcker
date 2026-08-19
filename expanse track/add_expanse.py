from database import create_connection
from datetime import date

def add_expense():
    conn = create_connection()
    cursor = conn.cursor()

    expense_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if expense_date.strip() == "":
        expense_date = str(date.today())

    category = input("Enter category (e.g. Food, Travel, Bills): ")
    amount = float(input("Enter amount: "))
    payment_mode = input("Enter payment mode (Cash/UPI/Card): ")
    description = input("Enter description (optional): ")

    cursor.execute("""
        INSERT INTO expenses (date, category, amount, payment_mode, description)
        VALUES (?, ?, ?, ?, ?)
    """, (expense_date, category, amount, payment_mode, description))

    conn.commit()
    conn.close()
    print("Expense added successfully!")

if __name__ == "__main__":
    add_expense()