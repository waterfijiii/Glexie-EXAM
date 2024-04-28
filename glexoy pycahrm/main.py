import os

# Function to display the menu
def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

# Function to process orders
def process_order(menu):
    order = {}
    while True:
        display_menu(menu)  # Sequential Structures (Display menu)
        choice = input("Enter your choice (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        if choice in menu:  # Decision Structures (if-else)
            quantity = input(f"Enter quantity for {choice}: ")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Quantity must be a positive integer.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
            order[choice] = order.get(choice, 0) + quantity
        else:
            print("Invalid choice. Please try again.")

    return order

# Function to generate invoice
def generate_invoice(order, menu):
    total_cost = 0
    invoice_details = []
    for item, quantity in order.items():
        cost = menu[item] * quantity
        invoice_details.append(f"{item}: {quantity} x ${menu[item]} = ${cost}")
        total_cost += cost
    invoice_details.append(f"Total: ${total_cost}")
    return invoice_details

# Function to write invoice to a text file and display invoice details
def write_to_file_and_display(invoice_details):
    print("Invoice Details:")
    for line in invoice_details:
        print(line)  # String Methods
    file_path = os.path.join(os.getcwd(), "invoice.txt")  # Text File Manipulation (Creating file path)
    with open(file_path, "w") as file:
        for line in invoice_details:
            file.write(line + "\n")  # Text File Manipulation (Writing to file)
    print(f"Invoice saved to '{file_path}'.")

# Main program
def main():
    menu = {'Bingka': 5, 'Puto': 8, 'Suman': 4}
    order = process_order(menu)
    invoice_details = generate_invoice(order, menu)
    write_to_file_and_display(invoice_details)  # Program Modularization
    print("Order processed successfully.")

if __name__ == "__main__":
    main()
