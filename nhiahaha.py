import random
import datetime
import json
import os

transactions = []
transactions_file = 'transactions.json'
history_log = []
total_sales_today = 0

car_list = {
        1: {
            "model": "MissyuBibi GT400",
            "price": "$30,000",
            "stock": 5
        },
        2: {
            "model": "MissyuBibi Alpha 6000",
            "price": "$40,000",
            "stock": 3
        },
        3: {
            "model": "MissyuBibi 2nd Gen Alpha 6000",
            "price": "$25,000",
            "stock": 7
        },
        4: {
            "model": "MissyuBibi 'NHIA' Limited Edition",
            "price": "$50,000",
            "stock": 2
        }
    }

pending_payments = []


class Transaction:
    def __init__(self,
                     car,
                     name,
                     number,
                     serial_num,
                     quantity,
                     payment_method,
                     warranty=30,
                     downpayment='',
                     payment=''):
            self.car = car
            self.name = name
            self.number = number
            self.serial_num = serial_num
            self.quantity = quantity
            self.payment_method = payment_method
            self.payment = payment
            self.downpayment = downpayment
            self.warranty = 30
            self.date_of_transaction = datetime.datetime.now().strftime("%x")

def __str__(self):
            return f"Car: {self.car}, Name: {self.name}, Number: {self.number}, Serial Number: {self.serial_num}, Quantity: {self.quantity}, Payment Method: {self.payment_method}, Warranty: {self.warranty} days, Payment:, {self.payment}, Downpayment: {self.downpayment}, Date of Transaction: {self.date_of_transaction}"


def load_transactions():
        if os.path.exists(transactions_file):
            try:
                with open(transactions_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error reading the file: {e}")
                return []
        return []


def save_transactions_to_json():
        with open(transactions_file, 'w') as file:
            transactions_data = [{
                'car':
                transaction.car,
                'name':
                transaction.name,
                'number':
                transaction.number,
                'serial_num':
                transaction.serial_num,
                'quantity':
                transaction.quantity,
                'payment': 
                f"${transaction.payment:,.0f}",
                'payment_method':
                transaction.payment_method,
                'downpayment':
                transaction.downpayment,
                'warranty':
                transaction.warranty,
                'date_of_transaction':
                transaction.date_of_transaction
            } for transaction in transactions]
            json.dump(transactions_data, file, indent=4)


def save_transactions():
        file_name = input("Enter the name of the file (without extension): ")
        file_extension = input("Enter the file extension (json or txt): ").lower()

        if file_extension not in ['json', 'txt']:
            print("Invalid file extension. Please enter either 'json' or 'txt'.")
            return save_transactions()

        if file_extension == 'json':
            save_transactions_to_json()
            print(f"Transactions saved to {file_name}.json")
        elif file_extension == 'txt':
            with open(f"{file_name}.txt", 'w') as file:
                for transaction in transactions:
                    file.write(f"Car: {transaction.car}\n")
                    file.write(f"Name: {transaction.name}\n")
                    file.write(f"Contact No.: {transaction.number}\n")
                    file.write(f"Serial Number: {transaction.serial_num}\n")
                    file.write(f"Quantity: {transaction.quantity}\n")
                    file.write(f"Payment Method: {transaction.payment_method}\n")
                    file.write(f"Payment: ${transaction.payment:,.0f}\n")
                    file.write(f"Downpayment: {transaction.downpayment}\n")
                    file.write(f"Warranty: {transaction.warranty} days\n")
                    file.write(
                        f"Transaction Date: {transaction.date_of_transaction}\n")
                    file.write("-" * 30 + "\n")
                print(f"Transactions saved to {file_name}.txt")


def purchase_car():
        global total_sales_today
        print("\n========== MISSYUBIBI CAR DEALERSHIP ==========")
        print("Choose a car to purchase:")
        available_cars = {k: v for k, v in car_list.items() if v['stock'] > 0}

        if not available_cars:
            print("All cars are out of stock. No purchase can be made.")
            return

        for idx, car in available_cars.items():
            print(
                f"\n{idx}. {car['model']} \nPrice: {car['price']} \nStock: {car['stock']}"
            )

        print("\n10. Cancel Purchase")
        print("================================================")

        car_choice = input("Enter car number (1-5): ")

        if car_choice == '10':
            return

        try:
            car_choice = int(car_choice)
            if car_choice not in available_cars:
                print("Invalid choice. Please select a valid car number.")
                return
        except ValueError:
            print("Invalid input. Please select a valid car number.")
            return

        selected_car = available_cars[car_choice]
        car_name = selected_car['model']
        price_per_car = float(selected_car['price'].replace("$", "").replace(",", ""))
        stock_available = selected_car['stock']

        quantity = int(
            input(
                f"How many {car_name}s would you like to buy? (Available stock: {stock_available}): "
            ))
        if quantity > stock_available:
            print(f"Sorry, we only have {stock_available} {car_name}s in stock.")
            return

        selected_car['stock'] -= quantity
        total_price = price_per_car * quantity

        print("\nChoose a payment method:")
        print("1. Cash")
        print("2. Credit")
        print("3. Debit")
        print("4. Downpayment")
        payment_choice = input("Enter payment method number (1-4): ")

        name = input("Enter your name: ")
        number = input("Enter your contact number: ")
        serial_num = random.randint(100000, 999999)

        payment_method = ''
        downpayment = 0
        payment = 0

        if payment_choice == '1':
            payment_method = 'Cash'
            payment = total_price
            total_sales_today += payment
        elif payment_choice == '2':
            payment_method = 'Credit'
            payment = total_price
            total_sales_today += payment
        elif payment_choice == '3':
            payment_method = 'Debit'
            payment = total_price
            total_sales_today += payment
        elif payment_choice == '4':
            payment_method = 'Downpayment'
            downpayment = float(input("Enter downpayment amount: "))
            if downpayment > total_price:
                print(
                    "Downpayment cannot exceed the total price. Please try again.")
                return

            remaining_balance = total_price - downpayment
            pending_payments.append({
                'name': name,
                'car': car_name,
                'downpayment': downpayment,
                'remaining_balance': remaining_balance
            })
            total_sales_today += downpayment
        else:
            print("Invalid choice. Please select a valid payment method.")
            return

        transaction = Transaction(
            car_name,
            name,
            number,
            serial_num,
            quantity,
            payment_method,
            payment=payment,
            downpayment=downpayment
        )
        transactions.append(transaction)

        print("\nTransaction Successful:")
        print(f"Car: {transaction.car}")
        print(f"Name: {transaction.name}")
        print(f"Contact No.: {transaction.number}")
        print(f"Serial Number: {transaction.serial_num}")
        print(f"Quantity: {transaction.quantity}")
        print(f"Payment Method: {transaction.payment_method}")
        print(f"Payment: ${transaction.payment:,.2f}")
        print(f"Downpayment: ${transaction.downpayment:,.2f}")
        print(f"Warranty: {transaction.warranty} days")
        print(f"Transaction Date: {transaction.date_of_transaction}")

        history_log.append(
            f"\n- {name.capitalize()} purchased {quantity} {car_name}(s) on {transaction.date_of_transaction} (Serial Number: {serial_num}, Payment Method: {payment_method})"
        )



def view_all_transactions():
        if not transactions:
            print("No transactions to display.")
            return

        for transaction in transactions:
            print("\nTransaction History:")
            print(f"Car: {transaction['car']}")
            print(f"Name: {transaction['name']}")  
            print(f"Contact No.: {transaction['number']}")
            print(f"Serial Number: {transaction['serial_num']}")
            print(f"Warranty: {transaction['warranty']} days")
            print(f"Transaction Date: {transaction['date_of_transaction']}")
            print("-" * 30)

        history_log.append("\n- Viewed all transactions")


def search_transaction():
        print("\n========== Search Transactions ==========")
        print("Search by:")
        print("1. Name")
        print("2. Number")
        print("3. Serial Number")
        choice_customer = input("Enter choice (1-3): ")

        if choice_customer == '1':
            search_name = input("Enter name: ")
            found = False
            for transaction in transactions:
                if search_name.lower() == transaction.name.lower():
                    print(transaction)
                    found = True
            if not found:
                print("Name not found.")
        elif choice_customer == '2':
            search_number = input("Enter contact number: ")
            found = False
            for transaction in transactions:
                if search_number == transaction.number:
                    print(transaction)
                    found = True
            if not found:
                print("Contact number not found.")
        elif choice_customer == '3':
            search_serial = input("Enter serial number: ")
            found = False
            for transaction in transactions:
                if str(search_serial) == str(transaction.serial_num):
                    print(transaction)
                    found = True
            if not found:
                print("Serial number not found.")
        else:
            print("Invalid choice.")

        history_log.append(
            f"\n- Searched transactions by {['Name', 'Number', 'Serial Number'][int(choice_customer)-1]}"
        )


def available_refund():
        if not transactions:
            print("No transactions found.")
            return

        print("\n========== Check Refund Eligibility ==========")
        print("You can search by: ")
        print("1. Name")
        print("2. Contact Number")
        print("3. Serial Number")
        search_choice = input("Enter your choice (1-3): ")

        if search_choice == '1':
            search_name = input("Enter your name: ")
            found = False
            for transaction in transactions:
                if search_name.lower() == transaction.name.lower():
                    if 1 <= transaction.warranty <= 30:
                        print(
                            f"Car {transaction.car} with Serial Number {transaction.serial_num} can still be refunded."
                        )
                    else:
                        print(
                            f"Car {transaction.car} with Serial Number {transaction.serial_num} warranty has ended, cannot be refunded."
                        )
                    found = True
            if not found:
                print("No transaction found for this name.")

        elif search_choice == '2':
            search_number = input("Enter your contact number: ")
            found = False
            for transaction in transactions:
                if search_number == transaction.number:
                    if 1 <= transaction.warranty <= 30:
                        print(
                            f"Car {transaction.car} with Serial Number {transaction.serial_num} can still be refunded."
                        )
                    else:
                        print(
                            f"Car {transaction.car} with Serial Number {transaction.serial_num} warranty has ended, cannot be refunded."
                        )
                    found = True
            if not found:
                print("No transaction found for this contact number.")

        elif search_choice == '3':
            search_serial = input("Enter your serial number: ")
            found = False
            for transaction in transactions:
                if str(search_serial) == str(transaction.serial_num):
                    if 1 <= transaction.warranty <= 30:
                        print(
                            f"Car {transaction.car} with Serial Number {transaction.serial_num} can still be refunded."
                        )
                    else:
                        print(
                            f"Car {transaction.car} with Serial Number {transaction.serial_num} warranty has ended, cannot be refunded."
                        )
                    found = True
            if not found:
                print("No transaction found for this serial number.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        history_log.append("\n- Checked refund eligibility")


def manage_cars():
        print("\n======== Manage Cars ========")
        print("1. View Cars")
        print("2. Add Car")
        print("3. Remove Car")
        print("4. Update Car Stock")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            list_sales(car_list)
        elif choice == '2':
            model = input("Enter model name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))
            car_id = len(car_list) + 1
            car_list[car_id] = {"model": model, "price" : f"${price:,.0f}", "stock": stock}
            print(f"Car added with ID: {car_id}")
        elif choice == '3':
            car_id = int(input("Enter car ID to remove: "))
            if car_id in car_list:
                del car_list[car_id]
                print(f"Car with ID {car_id} removed.")
            else:
                print("Car ID not found.")
        elif choice == '4':
            car_id = int(input("Enter car ID to update stock: "))
            if car_id in car_list:
                new_stock = int(input("Enter new stock: "))
                car_list[car_id]['stock'] = new_stock
                print(f"Stock for car ID {car_id} updated.")
            else:
                print("Car ID not found.")
        else:
            print("Invalid choice. Please try again.")

        history_log.append("\n- Managed Cars")


def finance_report():
    print("\n======== Finance Report ========")

    global total_sales_today

    total_sales = 0
    pending_sales = sum(payment['remaining_balance'] for payment in pending_payments)

    for transaction in transactions:
        if isinstance(transaction, Transaction):
            if transaction.date_of_transaction == datetime.datetime.now().strftime("%x"):
                total_sales_today += transaction.payment or 0
            total_sales += transaction.payment or 0
        elif isinstance(transaction, dict):
            payment = transaction.get('payment', 0)
            transaction_date = transaction.get('date_of_transaction', '')
            if transaction_date == datetime.datetime.now().strftime("%x"):
                total_sales_today += payment
            total_sales += payment

    print(f"Total Sales (Including All Payments): ${total_sales:,.2f}")
    print(f"Pending Payments (Remaining Balances): ${pending_sales:,.2f}")
    print(f"Today's Total Revenue (Payments Made Today): ${total_sales_today:,.2f}")

    if pending_sales > 0:
        print("\nPending Payments (Not Fully Paid):")
        for payment in pending_payments:
            print(f"Customer: {payment['name']}, Car: {payment['car']}, "
                  f"Downpayment: ${payment['downpayment']:,.2f}, "
                  f"Remaining Balance: ${payment['remaining_balance']:,.2f}")
    else:
        print("\nNo pending payments.")

    history_log.append("- Generated Finance Report")

def view_action_history():
        if history_log:
            print("\n========== Action History ==========")
            for action in history_log:
                print(action)
        else:
            print("No action history available.")

        history_log.append("\n- Checked Action History")


def list_sales(car_list):
        for car_id, car_details in car_list.items():
            model = car_details["model"]
            price = car_details["price"]
            stock = car_details["stock"]

            formatted_price = f"${price:,.2f}"

            print(
                f"\nModel: {model}\nPrice: {formatted_price}\nStock: {stock} units available\n"
            )


def main():
        global transactions
        transactions = load_transactions()

        while True:
            print("\n======== MISSYUBIBI CAR DEALERSHIP ========")
            print("1. Purchase Car")
            print("2. View All Transactions")
            print("3. Search Transaction")
            print("4. Available Refunds")
            print("5. Save Transactions to File")
            print("6. Clear All Transactions")
            print("7. View Action History")
            print("8. Manage Cars")
            print("9. Finance Report")
            print("10. Exit")

            choice = input("\nEnter choice (1-11): ")

            if choice == '1':
                purchase_car()
            elif choice == '2':
                view_all_transactions()
            elif choice == '3':
                search_transaction()
            elif choice == '4':
                available_refund()
            elif choice == '5':
                save_transactions()
            elif choice == '6':
                transactions.clear()
                print("\nAll transactions have been cleared.")
            elif choice == '7':
                view_action_history()
            elif choice == '8':
                manage_cars()
            elif choice == '9':
                finance_report()
            elif choice == '10':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()