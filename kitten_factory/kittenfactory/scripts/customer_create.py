import requests
import random
from faker import Faker

# Assuming the Customer model is defined in Django as follows:
# class Customer(models.Model):
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     email = models.EmailField()
#     phoneNumber = models.CharField(max_length=15)
#     address = models.CharField(max_length=75, null=True)

# Initialize Faker to generate random data
fake = Faker()

def create_random_customer():
    """Generate a random customer dictionary based on the Customer model."""
    return {
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'email': fake.email(),
        'phoneNumber': fake.phone_number(),
        'address': fake.address()
    }

def send_customer_to_api(customer):
    """Send a customer dictionary to an API endpoint."""
    url = 'http://127.0.0.1:8000/kittenfactory/customer/'  # Replace with the actual API URL
    response = requests.post(url, json=customer)
    return response

def main():
    for _ in range(20):
        customer = create_random_customer()
        response = send_customer_to_api(customer)
        print(f'Status Code: {response.status_code}, Response: {response.json()}')

if __name__ == "__main__":
    main()