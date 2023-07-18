from faker import Faker
import random

fake = Faker()

def generate_investor():
    return {
        "name": fake.company(),
        "type": random.choice(["Bank", "NBFC", "Angel", "Peer to Peer", "Venture Capitalist", "Personal"]),
        "address": {
            "country": fake.country(),
            "state": fake.state(),
            "city": fake.city(),
            "pincode": fake.postcode(),
            "address": fake.address()
        }
    }