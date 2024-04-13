import requests
import random
from datetime import date

# Configuration
API_URL = "http://127.0.0.1:8000/kittenfactory/api/order/"
HEADERS = {'Content-Type': 'application/json'}
CUSTOMER_COUNT = 36  # Assuming you have customers with IDs 1 through 36
PRODUCT_IDS = [1, 2, 3, 4, 5]  # Assuming some product IDs

def create_order(customer_id, product_id, quantity, order_date, price):
    """ Create an order data dictionary. """
    return {
        'customer': customer_id,
        'product': product_id,
        'quantity': quantity,
        'date': order_date.strftime("%Y-%m-%d"),  # Format date as YYYY-MM-DD
        'price': str(price)  # Convert decimal to string to avoid JSON serialization issues
    }

def send_order(order_data):
    """ Send the order to the API. """
    response = requests.post(API_URL, json=order_data, headers=HEADERS)
    if response.status_code == 201:
        print("Order created successfully:", response.json())
    else:
        print("Failed to create order:", response.status_code, response.text)

# Generate and send orders
for _ in range(75):  # Create 10 random orders
    customer_id = random.randint(1, CUSTOMER_COUNT)
    product_id = random.choice(PRODUCT_IDS)
    quantity = random.randint(1, 3)  # Random quantity between 1 and 10
    order_date = date.today()
    price = random.uniform(200.00, 3000.00)  # Random price between $20 and $100

    order = create_order(customer_id, product_id, quantity, order_date, price)
    send_order(order)