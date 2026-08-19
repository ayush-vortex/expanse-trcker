from database import create_connection
import pandas as pd

def view_expenses():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No expenses found.")
    else:
        print(df)
        print(f"\nTotal expenses: {len(df)}")
        print(f"Total amount spent: ₹{df['amount'].sum()}")

if __name__ == "__main__":
    view_expenses()