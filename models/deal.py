from faker import Faker
import random

fake = Faker()

def generate_deal(borrower_id):
    return {
        "borrower_id": borrower_id,
        "amount": random.randint(1, 1_000) * 1_000_000,
        "status": random.choice(["NEW", "IN PROGRESS", "CLOSED", "STALE", "LOCKED", "TURNED DOWN"])
    }