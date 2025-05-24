import mysql.connector

class ATM:
    def __init__(self, user_id, user_name, pin, balance, conn):
        self.user_id = user_id
        self.user_name = user_name
        self.pin = pin
        self.balance = balance
        self.conn = conn
        self.cursor = conn.cursor()

    def update_balance_in_db(self):
        self.cursor.execute(
            "UPDATE users SET balance = %s WHERE user_id = %s",
            (self.balance, self.user_id)
        )
        self.conn.commit()

    def show_menu(self):
        print(f"\n===== Welcome, {self.user_name}! =====")
        print("1. Balance Enquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Money Transfer")
        print("5. Change ATM PIN")
        print("6. Exit")

    def balance_enquiry(self):
        print(f"Your current balance is ₹{self.balance:.2f}")

    def withdraw_cash(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Enter a valid amount.")
            elif amount > self.balance:
                print("Insufficient Balance.")
            else:
                self.balance -= amount
                self.update_balance_in_db()
                print(f" ₹{amount:.2f} withdrawn. Remaining Balance: ₹{self.balance:.2f}")
        except ValueError:
            print("Invalid input.")

    def deposit_cash(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("Enter a valid amount.")
            else:
                self.balance += amount
                self.update_balance_in_db()
                print(f" ₹{amount:.2f} deposited. Updated Balance: ₹{self.balance:.2f}")
        except ValueError:
            print("Invalid input.")

    def transfer_money(self):
        recipient_id = input("Enter recipient's 12-digit user ID: ")
        try:
            amount = float(input("Enter amount to transfer: ₹"))
            if amount <= 0:
                print(" Enter a valid amount.")
            elif amount > self.balance:
                print("Insufficient Balance.")
            else:
                # Check recipient by user_id
                self.cursor.execute("SELECT balance FROM users WHERE user_id = %s", (recipient_id,))
                rec =self.cursor.fetchone()
                if not rec:
                    print(" Recipient not found.")
                    return
                new_rec_balance = float(rec[0]) + amount
                self.cursor.execute("UPDATE users SET balance = %s WHERE user_id = %s", (new_rec_balance, recipient_id))

                self.balance -= amount
                self.update_balance_in_db()
                print(f"₹{amount:.2f} transferred to user ID {recipient_id}. Remaining Balance: ₹{self.balance:.2f}")
        except ValueError:
            print(" Invalid input.")

    def change_pin(self):
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            self.cursor.execute("UPDATE users SET pin = %s WHERE user_id = %s", (new_pin, self.user_id))
            self.conn.commit()
            print("PIN changed successfully.")
        else:
            print("Invalid PIN format.")

# --- SQL Connection ---
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",     
    password="your_password",
    database="database_name"
)

cursor = conn.cursor()

# --- ATM Login ---
print(" ATM Login")
entered_id = input("Enter your User ID: ")
entered_pin = input("Enter your 4-digit PIN: ")

cursor.execute("SELECT user_id, user_name, pin, balance FROM users WHERE user_id = %s", (entered_id,))
user_data = cursor.fetchone()

if user_data and entered_pin == user_data[2]:
    atm_user = ATM(user_id=user_data[0], user_name=user_data[1], pin=user_data[2], balance=float(user_data[3]), conn=conn)
    
    while True:
        atm_user.show_menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            atm_user.balance_enquiry()
        elif choice == '2':
            atm_user.withdraw_cash()
        elif choice == '3':
            atm_user.deposit_cash()
        elif choice == '4':
            atm_user.transfer_money()
        elif choice == '5':
            atm_user.change_pin()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
else:
    print(" Login failed. Invalid credentials.")

conn.close()
