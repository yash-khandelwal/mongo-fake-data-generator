from faker import Faker
import random

fake = Faker()

def generate_borrower():
    return {
        "name": fake.company(),
        "type": random.choice(["Individual", "Partnership Firm", "Company", "Trusts", "Family"]),
        "rating": int((4 + random.random()) * 10) / 10,
        "revenue": random.randint(1, 1_000) * 10_000_000,
        "address": {
            "country": fake.country(),
            "state": fake.state(),
            "city": fake.city(),
            "pincode": fake.postcode(),
            "address": fake.address()
        }
    }