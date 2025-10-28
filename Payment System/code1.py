

import time
from datetime import datetime, date

# -------------------------
# Simple in-memory "database"
# -------------------------
users = {}  # key: mps_id, value: dict with user info
next_mps_num = 100001  # simple counter for MPS IDs

# Constants for daily rules
DAILY_TX_LIMIT = 5
DAILY_AMOUNT_LIMIT = 20000
MAX_ATTEMPTS_AFTER_LIMIT = 3

# -------------------------
# Helper functions
# -------------------------
def today_date_str():
    """Return today's date as a string like '2025-10-27'."""
    return date.today().isoformat()

def gen_mps_id():
    """Generate a simple MPS ID like 'MPS100001', 'MPS100002', ..."""
    global next_mps_num
    mps_id = f"MPS{next_mps_num}"
    next_mps_num += 1
    return mps_id

def reset_daily_if_needed(user):
    """Reset daily counters if the stored date is not today."""
    today_str = today_date_str()
    if user["daily_date"] != today_str:
        user["daily_date"] = today_str
        user["daily_count"] = 0
        user["daily_amount"] = 0
        user["limit_attempts"] = 0
        user["locked"] = False  # new day -> unlock

def register_user():
    print("\n-- Register User --")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    account = input("Bank Account Number: ").strip()

    # Allow user to choose initial balance or default to 50,000
    bal_raw = input("Initial Balance (press Enter for 50000): ").strip()
    if bal_raw == "":
        balance = 50000
    else:
        try:
            balance = int(bal_raw)
            if balance < 0:
                print("Balance cannot be negative. Using 50000.")
                balance = 50000
        except ValueError:
            print("Invalid number. Using 50000.")
            balance = 50000

    mps_id = gen_mps_id()
    users[mps_id] = {
        "name": name,
        "phone": phone,
        "account": account,
        "balance": balance,
        "transactions": [],     # list of dicts: {"id", "type", "amount", "time"}
        "daily_date": today_date_str(),
        "daily_count": 0,
        "daily_amount": 0,
        "limit_attempts": 0,
        "locked": False
    }

    print(f"\nUser registered successfully! Your MPS ID is: {mps_id}")

def debit():
    print("\n-- Debit --")
    mps_id = input("Enter MPS ID: ").strip()
    if mps_id not in users:
        print("Invalid MPS ID.")
        return

    user = users[mps_id]
    reset_daily_if_needed(user)

    if user["locked"]:
        print("User is locked for today due to exceeding daily limit.")
        return

    # Get amount
    amt_raw = input("Enter amount (₹): ").strip()
    try:
        amount = int(amt_raw)
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be positive.")
        return

    # Check balance
    if amount > user["balance"]:
        print("Insufficient balance.")
        return

    # Check daily rules
    would_exceed_count = (user["daily_count"] + 1) > DAILY_TX_LIMIT
    would_exceed_amount = (user["daily_amount"] + amount) > DAILY_AMOUNT_LIMIT

    if would_exceed_count or would_exceed_amount:
        # Daily limit reached -> count an attempt
        user["limit_attempts"] += 1
        remaining = MAX_ATTEMPTS_AFTER_LIMIT - user["limit_attempts"]
        if user["limit_attempts"] >= MAX_ATTEMPTS_AFTER_LIMIT:
            user["locked"] = True
            print("Daily limit reached. 3 attempts used. You are locked for the rest of the day.")
        else:
            print(f"Daily limit reached. Attempt {user['limit_attempts']}/3. Remaining attempts today: {remaining}.")
        return

    # If allowed, perform debit
    user["balance"] -= amount
    user["daily_count"] += 1
    user["daily_amount"] += amount

    # Create a simple transaction record
    txn_id = f"TXN{int(time.time() * 1000)}"
    txn = {
        "id": txn_id,
        "type": "DEBIT",
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    user["transactions"].append(txn)

    print(f"Debit successful! [{txn_id}] DEBIT ₹{amount} on {txn['time']}")
    print(f"Remaining balance: ₹{user['balance']}")

def show_last_10():
    print("\n-- Last 10 Transactions --")
    mps_id = input("Enter MPS ID: ").strip()
    if mps_id not in users:
        print("Invalid MPS ID.")
        return

    user = users[mps_id]
    txns = user["transactions"][-10:]  # last 10
    if not txns:
        print("No transactions yet.")
        return

    # Show newest first
    for t in reversed(txns):
        print(f"[{t['id']}] {t['type']} ₹{t['amount']} on {t['time']}")

def admin_summary():
    print("\n-- Admin: User Count & Details --")
    count = len(users)
    print(f"Total Users: {count}")
    if count == 0:
        return

    print("\nName                          Phone           Account No        MPS ID")
    print("-" * 75)
    for mps_id, u in users.items():
        name = u["name"]
        phone = u["phone"]
        acc = u["account"]
        print(f"{name:<30} {phone:<15} {acc:<18} {mps_id}")

def main_menu():
    print("\n=== Manipal Payment System (Beginner) ===")
    print("1. Register User")
    print("2. Debit")
    print("3. View Last 10 Transactions")
    print("4. Admin: User Count & Details")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            debit()
        elif choice == "3":
            show_last_10()
        elif choice == "4":
            admin_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
