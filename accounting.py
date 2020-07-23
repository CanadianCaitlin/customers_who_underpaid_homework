
#create function takes parameter: order txt file
#open file
#loop in file to seperate strings
#if customer payment is greater than cost, return print statement
#elif customer payment is less than code, return print statement
#else pass

MELON_COST = 1.00

def customer_payment(payment_file):
    payment_data = open(payment_file)

    for line in payment_data:
        order = line.split('|')
        customer_name = order[1]
        customer_melons = float(order[2])
        customer_paid = float(order[3])

        correct_cost = customer_melons * MELON_COST
        payment_owed = correct_cost - customer_paid
        over_payment = customer_paid - correct_cost

        if correct_cost > customer_paid:
            print(f"{customer_name} paid ${customer_paid}, but the correct cost is ${correct_cost}. The customer needs to pay ${payment_owed}.")

        elif correct_cost < customer_paid:
            print(f"{customer_name} paid ${customer_paid}, but the correct cost is ${correct_cost}. The customer needs to recieve ${over_payment}.")

        else:
            pass

    payment_file.close()

customer_payment("customer-orders.txt")

# MELON_COST = 1.00


# def print_payment_status(payment_data_filename):
#     """Calculate cost of melons and determine who has underpaid."""

#     payment_data = open(payment_data_filename) # open the file

#     # Iterate over lines in file
#     for line in payment_data:
#         # Split line by '|' to get a list of strings
#         order = line.split('|')

#         # Get customer's full name
#         full_name = order[1]

#         # Split `customer_name` by space (' ') to get
#         # a list of [first_name, last_name].
#         #
#         # Then, assign first name (at index 0) to `customer_first`
#         first_name = full_name.split(" ")[0]

#         # Get no. of melons in the order and amount customer paid
#         melons_qty = float(order[2])  # also ok to typecast melons_qty as an int
#         amt_paid = float(order[3])

#         # Calculate expected price of customer's order
#         expected_price = melons_qty * MELON_COST

#         # Print general payment info
#         print(f"{full_name} paid ${amt_paid:.2f}, expected",
#               f"${expected_price:.2f}")

#         # Print payment status
#         #
#         # If customer overpaid, print that they've overpaid for their melons. If
#         # customer underpaid, print that they've underpaid for their melons.
#         if expected_price < amt_paid:
#             print(f"{first_name} has overpaid for their melons.")

#         elif expected_price > amt_paid:
#             print(f"{first_name} has underpaid for their melons.")

#     # Close the file
#     payment_data.close()


# # Call the function
# print_payment_status("customer-orders.txt")
 