from database import create_connection
import pandas as pd
import matplotlib.pyplot as plt

def analyze():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    df['date'] = pd.to_datetime(df['date'])

    # 1. Category-wise total spending
    category_totals = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    print("Category-wise spending:")
    print(category_totals)

    # 2. Payment mode breakdown
    payment_totals = df.groupby('payment_mode')['amount'].sum()
    print("\nPayment mode-wise spending:")
    print(payment_totals)

    # 3. Highest single expense
    top_expense = df.loc[df['amount'].idxmax()]
    print(f"\nHighest single expense: ₹{top_expense['amount']} on {top_expense['category']} ({top_expense['description']})")

    # 4. Plot: category-wise bar chart
    category_totals.plot(kind='bar', color='skyblue')
    plt.title("Spending by Category")
    plt.ylabel("Amount (₹)")
    plt.xlabel("Category")
    plt.tight_layout()
    plt.savefig("category_spending.png")
    print("\nChart saved as category_spending.png")

    # 5. Daily spending trend
    daily_totals = df.groupby('date')['amount'].sum()
    plt.figure()
    daily_totals.plot(kind='line', marker='o', color='green')
    plt.title("Daily Spending Trend")
    plt.ylabel("Amount (₹)")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("daily_trend.png")
    print("Trend chart saved as daily_trend.png")

if __name__ == "__main__":
    analyze()