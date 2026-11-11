from database import create_connection
import sys
import pandas as pd

# Windows consoles default to cp1252, which cannot encode the rupee sign (Rs).
# Reconfigure stdout to UTF-8 so printing never crashes on Windows.
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

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