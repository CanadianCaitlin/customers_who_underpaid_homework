
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
    
    # payment_file.close()

customer_payment("customer-orders.txt")
 