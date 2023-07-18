from faker import Faker
import random

fake = Faker()

def generate_express_interest(investor_id, deal_id):
    return {
        "investor_id": investor_id,
        "deal_id": deal_id,
        "status": random.choice(["NEW", "IN PROGRESS", "CLOSED", "STALE", "LOCKED", "TURNED DOWN"])
    }