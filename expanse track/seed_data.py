from database import create_connection
import random
from datetime import date, timedelta

categories = ["Food", "Travel", "Bills", "Shopping", "Entertainment", "Groceries"]
payment_modes = ["UPI", "Cash", "Card"]

descriptions = {
    "Food": ["Lunch", "Dinner", "Snacks", "Zomato order"],
    "Travel": ["Auto fare", "Bus ticket", "Petrol", "Cab"],
    "Bills": ["Electricity bill", "Mobile recharge", "Internet bill"],
    "Shopping": ["Clothes", "Stationery", "Shoes"],
    "Entertainment": ["Movie", "Netflix", "Gaming"],
    "Groceries": ["Vegetables", "Monthly groceries", "Fruits"]
}

def seed_data(num_entries=15):
    conn = create_connection()
    cursor = conn.cursor()

    today = date.today()

    for _ in range(num_entries):
        days_ago = random.randint(0, 45)
        expense_date = str(today - timedelta(days=days_ago))

        category = random.choice(categories)
        amount = round(random.uniform(50, 2000), 2)
        payment_mode = random.choice(payment_modes)
        description = random.choice(descriptions[category])

        cursor.execute("""
            INSERT INTO expenses (date, category, amount, payment_mode, description)
            VALUES (?, ?, ?, ?, ?)
        """, (expense_date, category, amount, payment_mode, description))

    conn.commit()
    conn.close()
    print(f"{num_entries} dummy expenses added successfully!")

if __name__ == "__main__":
    seed_data(15)